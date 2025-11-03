import re
from collections import Counter

def word_count(text: str) -> dict:
    """Return case-insensitive word frequency dictionary."""
    if not text:
        return {}
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))

#carlos's code for normalize whitespace
def normalize_whitespace(text: str) -> str:
    """Collapse runs of whitespace (spaces/tabs/newlines) to single spaces and trim edges."""
    return " ".join(text.split())

def remove_punctuation(text: str) -> str:
    """Remove all punctuation from the text."""
    return re.sub(r'[^\w\s]', '', text)

def is_palindrome(text: str | None = None) -> bool: 
    """Check if the given text is a palindrome, ignoring case and non-alphanumeric characters."""
    if text is None:
        print("No text provided")
        return False 
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    if len(cleaned) < 2:
        return False
    return cleaned == cleaned[::-1]

def is_palindrome_number(num: int | None = None) -> bool:
    """Check if the given integer is a palindrome."""
    if num is None:
        print("No number provided") 
        return False
    str_num = str(num)
    if len(str_num) < 2:
        return False
    return str_num == str_num[::-1]

def reverse_words(text: str | None = None) -> str:
    """Reverse each word in the given text while ignoring extra spaces."""
    if not text:
        return ""
    # Split by whitespace (not ' ') to ignore leading/trailing/multiple spaces
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def capitalize_sentences(text: str | None = None) -> str:
    """Capitalize the first letter of each sentence, handling punctuation and whitespace."""
    if not text:
        return ""

    parts = re.split(r'([.?!])', text)
    result = []

    sentence = ""
    for part in parts:
        if part in ".?!":

            cleaned = sentence.strip()
            if cleaned:
                result.append(cleaned.capitalize() + part)
            sentence = ""
        else:

            sentence += part

    cleaned = sentence.strip()
    if cleaned:
        result.append(cleaned.capitalize())

    return " ".join(result)

