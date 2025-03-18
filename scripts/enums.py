from enums import Enum

class WordErrorType(Enum):
    """
    **TYPOGRAPHICAL** = "typographical" \\
    **PHONETIC** = "phonetic" \\
    **OMISSION** = "omission" \\
    **MIX** = "mix"
    """
    TYPOGRAPHICAL = "typographical"
    PHONETIC = "phonetic"
    OMISSION = "omission"
    MIX = "mix"

class TypographicalErrorType(Enum):
    """    
    **SWAP** = swap \\
    **DELETE** = delete \\
    **INSERT** = insert \\
    **REPLACE** = replace
    """
    SWAP = "swap"
    DELETE = "delete"
    INSERT = "insert"
    REPLACE = "replace"