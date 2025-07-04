import string

def checkStrength(pwd: str) -> bool:
    
    has_upper = any(c.isupper() for c in pwd)
    
    has_digit = any(c.isdigit() for c in pwd)
    
    has_special = any(c in string.punctuation for c in pwd)

    return has_upper and has_digit and has_special
    