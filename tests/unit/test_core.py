import textutils.core as c

#unique words (collaborative feature Carlos, Alex)
def test_unique_words_basic_sorted_case_insensitive():
    assert c.unique_words("blue red RED red Blue") == ["blue", "red"]

def test_unique_words_handles_punctuation_and_spaces():
    assert c.unique_words("Hi, world!! hi.") == ["hi", "world"]

def test_unique_words_empty_text():
    assert c.unique_words("") == []

def test_unique_words_normalizes_apostrophes():
    assert c.unique_words("Don't stop, dont stop!") == ["dont", "stop"]