import re
from collections import Counter
import unicodedata


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


def word_lengths(text: str | None = None) -> dict:
    """Return a dict mapping each *distinct word as written* to its length.

    Handles:
      - punctuation (ignored)
      - multiple whitespace / newlines
      - digits & underscores as part of words
      - Unicode words (e.g., café)
      - empty/None text gracefully
    """
    if not text:
        return {}

    # Normalize Unicode so things like "ﬁ" and accents are consistent
    text = unicodedata.normalize("NFKC", text)

    # \w is Unicode-aware in Python 3 and includes letters, digits, and _
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)

    # Use the words as they appear (case-sensitive) so "go" and "GO" are distinct keys
    return {w: len(w) for w in words}

import unicodedata

def strip_accents(text: str) -> str:
    """Return text with diacritic accents removed, preserving non-Latin scripts and symbols.
    
    Examples:
        "café déjà vu"     → "cafe deja vu"
        "ÉLÉPHANT"         → "ELEPHANT"
        "naïve façade"     → "naive facade"
        "こんにちは résumé ☕" → "こんにちは resume ☕"
    """
    if not text:
        return ""

    normalized = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return unicodedata.normalize("NFC", stripped)

def strip_accents(text: str) -> str:
    if not text:
        return ""
    normalized = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return unicodedata.normalize("NFC", stripped)

def slugify(text: str) -> str:
    """Convert text to lowercase, hyphen-separated, URL-safe slug."""
    if not text:
        return ""

    text = strip_accents(text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)   # remove punctuation & emoji
    text = re.sub(r"[\s-]+", "-", text)    # collapse only spaces & hyphens
    text = text.strip("-")
    return text

def camel_to_snake(text: str) -> str:
    if not text:
        return ""

    # Preserve leading and trailing underscores
    leading = re.match(r"^_+", text)
    trailing = re.search(r"_+$", text)
    leading = leading.group(0) if leading else ""
    trailing = trailing.group(0) if trailing else ""

    core = text.strip("_")
    core = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", core)
    core = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", core)
    core = core.lower()
    
    return f"{leading}{core}{trailing}"

def truncate(text: str, n: int) -> str:
    """Shorten text to n chars, adding '…' if needed."""
    if text is None:
        return ""
    if n <= 0:
        return "…"
    if len(text) <= n:
        return text
    if n == 1:
        return "…"

    slice_text = text[: n - 1]

    # Remove trailing non-word, non-space chars (e.g., emoji, punctuation).
    # If we removed something, keep any trailing space (e.g., "emoji …").
    # If we didn't remove anything, trim trailing spaces (e.g., "hello…").
   
    without_trailing_symbols = re.sub(r"[^\w\s]+$", "", slice_text)
    if without_trailing_symbols == slice_text:
        slice_text = slice_text.rstrip()
    else:
        slice_text = without_trailing_symbols

    return slice_text + "…"