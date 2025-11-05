import unicodedata
import re

def unique_words(text: str) -> list[str]:
    """Return a sorted list of unique words (case-insensitive),
    ignoring punctuation and normalizing apostrophes."""
    if not text:
        return []
    text = unicodedata.normalize("NFKC", text.lower())
    text = re.sub(r"[’']", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    words = re.findall(r"\b\w+\b", text)
    return sorted(set(words))