import random

from scripts.enums import WordErrorType, TypographicalErrorType
from scripts.constants import PHONETIC_REPLACEMENTS, KEYBOARD_NEIGHBORS, ALPHABET


def typographical_errors(text: str, level: float = 0.1, seed: int = 42) -> str:
    """
    Simulate typographical errors (keyboard mistakes).
    Introduces random errors like letter swaps, insertions, deletions, or replacements.
    """
    random.seed(seed)
    text = list(text)

    for i in range(len(text)):
        if random.random() < level/5:  # Probability increases with level
            # Randomly select an error type
            error_type = random.choice(
                [
                    TypographicalErrorType.SWAP,
                    TypographicalErrorType.DELETE,
                    TypographicalErrorType.INSERT,
                    TypographicalErrorType.REPLACE,
                ]
            )

            match error_type:
                case TypographicalErrorType.SWAP:
                    if i < len(text) - 1:
                        # Swap adjacent letters
                        text[i], text[i + 1] = text[i + 1], text[i]

                case TypographicalErrorType.DELETE:
                    # Delete the character (simulate a typo)
                    text[i] = ""  # Remove the character

                case TypographicalErrorType.INSERT:
                    # Insert a random character (simulate typing an extra letter)
                    random_char = random.choice(list(ALPHABET))
                    text.insert(i, random_char)
                    i += 1  # Skip the next character to avoid repeated insertions

                case TypographicalErrorType.REPLACE:
                    if text[i].lower() in KEYBOARD_NEIGHBORS:
                        text[i] = random.choice(KEYBOARD_NEIGHBORS[text[i].lower()])

    return "".join(text)


def phonetic_misspellings(text: str, level: float = 0.1, seed: int = 42) -> str:
    """
    Simulate phonetic misspellings (sound-based errors).
    - Level 1: Minor phonetic changes
    - Level 2: More phonetic changes
    - Level 3: Drift into text/chat language
    """
    random.seed(seed)
    words = text.split()
    for i in range(len(words)):
        word = words[i].lower()
        for key, values in PHONETIC_REPLACEMENTS.items():
            if (
                key in word and random.random() < level/5
            ):  # Probability increases with level
                words[i] = random.choice(values)
    return " ".join(words)


def simulate_drift(
    text: str, error_type: WordErrorType, level: float = 0.1, seed=42
) -> str:
    """
    Simulate drift based on the error type and level.
    """
    match error_type:
        case WordErrorType.TYPOGRAPHICAL:
            return typographical_errors(text=text, level=level, seed=seed)
        case WordErrorType.PHONETIC:
            return phonetic_misspellings(text=text, level=level, seed=seed)
        case WordErrorType.MIX:
            t1 = typographical_errors(text=text, level=level/2, seed=seed)
            t2 = phonetic_misspellings(text=t1, level=level/2, seed=seed)
            return t2
        case _:
            raise ValueError("Invalid error type. Choose 'typographical', 'phonetic'")
