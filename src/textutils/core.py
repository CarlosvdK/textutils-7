import re
from collections import Counter

def word_count(text: str) -> dict:
    """Return case-insensitive word frequency dictionary."""
    if not text:
        return {}
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))