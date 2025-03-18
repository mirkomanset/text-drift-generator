import random

from scripts.enums import WordErrorType


def typographical_errors(text, level=1):
    """
    Simulate typographical errors (keyboard mistakes).
    - Level 1: Minor typos
    - Level 2: Letters swapped
    - Level 3: Multiple errors
    """
    text = list(text)
    for i in range(len(text)):
        if random.random() < (0.1 * level):  # Probability increases with level
            # Swap with a nearby character (simulate keyboard mistake)
            if i < len(text) - 1:
                text[i], text[i + 1] = text[i + 1], text[i]
    return ''.join(text)

def phonetic_misspellings(text, level=1):
    """
    Simulate phonetic misspellings (sound-based errors).
    - Level 1: Minor phonetic changes
    - Level 2: More phonetic changes
    - Level 3: Drift into text/chat language
    """
    replacements = {
        'a': ['a', 'e', '@'],
        'e': ['e', '3'],
        'i': ['i', '1'],
        'o': ['o', '0'],
        'u': ['u', 'you'],
        'to': ['to', '2'],
        'for': ['for', '4'],
        'you': ['you', 'u'],
        'the': ['the', 'da', 'd@']
    }
    words = text.split()
    for i in range(len(words)):
        word = words[i].lower()
        for key, values in replacements.items():
            if key in word and random.random() < (0.1 * level):  # Probability increases with level
                words[i] = random.choice(values)
    return ' '.join(words)

def omission_errors(text, level=1):
    """
    Simulate omission errors (dropping letters).
    - Level 1: Minor omissions
    - Level 2: More omissions
    - Level 3: Severe omissions (e.g., "I c u tmrw")
    """
    text = list(text)
    for i in range(len(text)):
        if random.random() < (0.1 * level):  # Probability increases with level
            text[i] = ''  # Drop the character
    return ''.join(text)

def simulate_drift(text: str, error_type: WordErrorType, level:int=1):
    """
    Simulate drift based on the error type and level.
    """
    match error_type:
        case WordErrorType.TYPOGRAPHICAL:
            return typographical_errors(text, level)
        case WordErrorType.PHONETIC:
            return phonetic_misspellings(text, level)
        case WordErrorType.OMISSION:
            return omission_errors(text, level)

        case _:
            raise ValueError("Invalid error type. Choose 'typographical', 'phonetic', or 'omission'.")
