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
    assert c.is_palindrome("") == False  # empty string is not a palindrome in my opinion
    assert c.is_palindrome() == False
    
def test_is_palindrome_for_integers():
    assert c.is_palindrome_number(12321) == True
    assert c.is_palindrome_number(12345) == False
    assert c.is_palindrome_number(0) == False # single digit is not a palindrome in my opinion
    assert c.is_palindrome_number() == False 
    
def test_reverse_words():
    assert c.reverse_words("Hello World") == "olleH dlroW"
    assert c.reverse_words("  Leading and trailing spaces  ") == "gnidaeL dna gniliart secaps"
    assert c.reverse_words("") == ""
    assert c.reverse_words() == ""
    
def test_capitalize_sentences_starts_each_sentence_with_capital():
    text = "hello world. how are you? i'm fine!  spaces."
    assert c.capitalize_sentences(text) == "Hello world. How are you? I'm fine! Spaces."

def test_capitalize_sentences_handles_leading_whitespace():
    assert c.capitalize_sentences("   hi.  there.") == "Hi. There."