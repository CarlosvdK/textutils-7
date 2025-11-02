import textutils.core as c

def test_word_count_basic():
       text = "Red red BLUE"
       assert c.word_count(text) == {"red": 2, "blue": 1}

#Carlos's featur for normalize_whitespace branch
def test_normalize_whitespace_basic():
    assert c.normalize_whitespace("a   b\t c\n") == "a b c"
def test_normalize_whitespace_trims_edges():
    assert c.normalize_whitespace("   hello   ") == "hello"

# Sara - feature for remove_punctuation branch
def test_remove_punctuation():
    text_1 = "Hello, world! How are you? I'm doing a test."
    text_2 = "!!!...,,,;;;'''\"\"\""
    assert c.remove_punctuation(text_1) == "Hello world How are you Im doing a test"
    assert c.remove_punctuation(text_2) == "" #make sure all punctuation is removed and not changed to spaces
    
def test_is_palindrome_phrase():
    assert c.is_palindrome("A man a plan a canal Panama") == True
    assert c.is_palindrome("No 'x' in Nixon") == True
    assert c.is_palindrome("Hello, World!") == False