import textutils.core as c
import pytest

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
    

def test_word_lengths_maps_each_word_to_length():
    assert c.word_lengths("hi there") == {"hi": 2, "there": 5}
    assert c.word_lengths("hello, world!") == {"hello": 5, "world": 5}
    text = "one   two\nthree"
    assert c.word_lengths(text) == {"one": 3, "two": 3, "three": 5}
    assert c.word_lengths("go go GO") == {"go": 2, "GO": 2}
    assert c.word_lengths("") == {}
    assert c.word_lengths("abc123 var_name") == {"abc123": 6, "var_name": 8}
    assert c.word_lengths("café naïve") == {"café": 4, "naïve": 5}

def test_strip_accents_removes_diacritics():
    assert c.strip_accents("café déjà vu") == "cafe deja vu"
    assert c.strip_accents("fiancée jalapeño über naïve façade") == \
           "fiancee jalapeno uber naive facade"
    assert c.strip_accents("ÉLÉPHANT À LA CRÈME BRÛLÉE") == "ELEPHANT A LA CREME BRULEE"
    composed = "Cafe\u0301"  
    assert c.strip_accents(composed) == "Cafe"
    assert c.strip_accents("résumé 2.0!") == "resume 2.0!"
    assert c.strip_accents("café ☕ résumé 💼") == "cafe ☕ resume 💼"
    text = "こんにちは Москва résumé"
    assert c.strip_accents(text) == "こんにちは Москва resume"
    assert c.strip_accents("") == ""

def test_slugify_lowercase_hyphen_safe():
    assert c.slugify("Hello, World! 2025") == "hello-world-2025"
    assert c.slugify("Café déjà vu") == "cafe-deja-vu"
    assert c.slugify("Multiple    spaces") == "multiple-spaces"
    assert c.slugify("Symbols & punctuation!") == "symbols-punctuation"
    assert c.slugify("MiXeD CaSe Text") == "mixed-case-text"
    assert c.slugify("trailing---hyphens---") == "trailing-hyphens"
    assert c.slugify("underscores_are_okay") == "underscores_are_okay"
    assert c.slugify("Emoji ☕ test") == "emoji-test"
    assert c.slugify("") == ""


def test_slugify_collapses_hyphens_and_trims():
    assert c.slugify("  A---B  ") == "a-b"
    assert c.slugify("A--B--C") == "a-b-c"
    assert c.slugify("--Leading and trailing--") == "leading-and-trailing"
    assert c.slugify("   Spaces   and---hyphens  ") == "spaces-and-hyphens"
    assert c.slugify("Already-Slugified-Text") == "already-slugified-text"

@pytest.mark.parametrize(
    "src, dst",
    [
        ("CamelCase", "camel_case"),
        ("HTTPServerError", "http_server_error"),
        ("simple", "simple"),
        ("AWord", "a_word"),
        ("XMLHttpRequest", "xml_http_request"),
        ("parseJSON", "parse_json"),
        ("already_snake_case", "already_snake_case"),
        ("_PrivateVar", "_private_var"),
        ("Version2Update", "version2_update"),
        ("UserID123", "user_id123"),
        ("GetXValue", "get_x_value"),
        ("API", "api"),
        ("MyClass_", "my_class_"),
        ("", ""),
        ("tEsTiNgCaSe", "t_es_ti_ng_ca_se"),
    ],
)
def test_camel_to_snake_basic(src, dst):
    assert c.camel_to_snake(src) == dst

def test_truncate_shortens_to_n_chars_with_ellipsis_if_needed():
    assert c.truncate("hello world", 7) == "hello…"
    assert c.truncate("abcdef", 3) == "ab…"
    assert c.truncate("truncate me please", 10) == "truncate…"
    assert c.truncate("edgecase", 1) == "…"
    assert c.truncate("emoji 😊 test", 8) == "emoji …"
    assert c.truncate("", 5) == ""
    assert c.truncate("a", 1) == "a"
    assert c.truncate("a", 0) == "…"


def test_truncate_returns_same_if_short_enough():
    assert c.truncate("cat", 5) == "cat"
    assert c.truncate("hi", 2) == "hi"
    assert c.truncate("short", 10) == "short"
    assert c.truncate("", 1) == ""
    assert c.truncate("x", 1) == "x"

