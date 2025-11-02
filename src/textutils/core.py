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
