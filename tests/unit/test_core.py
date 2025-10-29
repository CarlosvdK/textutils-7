import textutils.core as c
def test_count_vowels():
    assert c.count_vowels("Hello World") == 3
    assert c.count_vowels("Python Programming") == 4
    assert c.count_vowels("BCDFG") == 0
    assert c.count_vowels("AEIOUaeiou") == 10