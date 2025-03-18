PHONETIC_REPLACEMENTS = {
    "a": ["a", "e", "@", "ah", "aa"],
    "e": ["e", "3", "ea", "eh"],
    "i": ["i", "1", "eye", "ai"],
    "o": ["o", "0", "oh", "oa"],
    "u": ["u", "you", "yoo", "oo"],
    "to": ["to", "2", "too", "t@"],
    "for": ["for", "4", "4r", "4u"],
    "you": ["you", "u", "yo", "y@u", "yoo"],
    "the": ["the", "da", "d@", "tha", "teh"],
    "and": ["and", "&", "n", "an"],
    "because": ["because", "bc", "bcz", "cos"],
    "see": ["see", "c", "sea", "se"],
    "are": ["are", "r", "aur", "ar"],
    "really": ["really", "rly", "rilly", "reely"],
    "people": ["people", "peeps", "ppl", "peepz"],
    "what": ["what", "wut", "wat"],
    "how": ["how", "hw", "h0w"],
    "know": ["know", "no", "kno", "n0"],
    "that": ["that", "dat", "th@t", "tha"],
    "would": ["would", "wd", "wld", "wud"],
    "going": ["going", "goin", "gng", "go@ing"],
    "today": ["today", "t0day", "tod@ay", "2day"],
    "here": ["here", "hr", "h3re"],
    "can": ["can", "ca", "cn", "k@n"],
    "me": ["me", "m3", "mi"],
    "good": ["good", "gd", "gr8", "gud"],
    "bad": ["bad", "b@d", "b4d", "badd"],
    "want": ["want", "wnt", "w@nt"],
    "love": ["love", "luv", "l0ve", "lve"],
    "hate": ["hate", "h8", "h8e"],
}

KEYBOARD_NEIGHBORS = {
    "q": ["w", "a", "s"],
    "w": ["q", "e", "a", "s", "d"],
    "e": ["w", "r", "s", "d", "f"],
    "r": ["e", "t", "d", "f", "g"],
    "t": ["r", "y", "f", "g", "h"],
    "y": ["t", "u", "g", "h", "j"],
    "u": ["y", "i", "h", "j", "k"],
    "i": ["u", "o", "j", "k", "l"],
    "o": ["i", "p", "k", "l"],
    "p": ["o", "l"],
    "a": ["q", "w", "s", "z"],
    "s": ["a", "w", "e", "d", "z", "x"],
    "d": ["s", "e", "r", "f", "x", "c"],
    "f": ["d", "r", "t", "g", "c", "v"],
    "g": ["f", "t", "y", "h", "v", "b"],
    "h": ["g", "y", "u", "j", "b", "n"],
    "j": ["h", "u", "i", "k", "n", "m"],
    "k": ["j", "i", "o", "l", "m"],
    "l": ["k", "o", "p"],
    "z": ["a", "s", "x"],
    "x": ["z", "s", "d", "c"],
    "c": ["x", "d", "f", "v"],
    "v": ["c", "f", "g", "b"],
    "b": ["v", "g", "h", "n"],
    "n": ["b", "h", "j", "m"],
    "m": ["n", "j", "k"],
}

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

EXAMPLE_STRING = "Artificial intelligence is revolutionizing the way we live and work. " \
"It is transforming industries by automating tasks, improving efficiency, and enhancing decision-making. " \
"As AI technology evolves, it opens up new possibilities for businesses and individuals alike. " \
"However, challenges remain in ensuring ethical use, data privacy, and fairness. " \
"As we move forward, it's crucial to balance innovation with responsibility to maximize the benefits while minimizing risks."
