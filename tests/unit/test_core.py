import textutils.core as c

def test_word_count_basic():
       text = "Red red BLUE"
       assert c.word_count(text) == {"red": 2, "blue": 1}

#Carlos's featur for normalize_whitespace branch
def test_normalize_whitespace_basic():
    assert c.normalize_whitespace("a   b\t c\n") == "a b c"
def test_normalize_whitespace_trims_edges():
    assert c.normalize_whitespace("   hello   ") == "hello"