def word_count(text):
    return 2

#carlos's code for normalize whitespace
def normalize_whitespace(text: str) -> str:
    """Collapse runs of whitespace (spaces/tabs/newlines) to single spaces and trim edges."""
    return " ".join(text.split())