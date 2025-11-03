import textutils.core as c

def test_mega_pipeline_with_my_functions():
    text = "  Héllo   Wórld!!! Café costs $123.   CamelCaseExample is COOL. A man a plan a canal Panama! Listen vs Silent.   "

    final_result = c.truncate(
        c.slugify(
            c.remove_punctuation(
                c.strip_accents(
                    c.normalize_whitespace(text)
                )
            )
        ),
        120
    )

    assert "hello-world" in final_result
    assert "cafe-costs-123" in final_result
    assert "camelcaseexample-is-cool" in final_result
    assert "a-man-a-plan-a-canal-panama" in final_result
    assert "listen-vs-silent" in final_result

    counts = c.word_count(c.strip_accents(text))
    assert counts.get("hello", 0) >= 1
    assert counts.get("world", 0) >= 1
    assert counts.get("cafe", 0) >= 1

    assert c.is_palindrome("A man a plan a canal Panama") is True
    assert c.is_palindrome("No 'x' in Nixon") is True
    assert c.is_palindrome("") is False

    assert c.is_anagram("Listen", "Silent") is True
    assert c.is_anagram("Hello", "Olelhh") is False

    assert c.reverse_words("Hello World") == "olleH dlroW"

    sim = c.compare_texts("hello world", "world hello")
    assert 0.45 <= sim < 1.0


    lens = c.word_lengths("test words")
    assert lens.get("test") == 4
    assert lens.get("words") == 5

    assert c.sentence_count("First. Second! Third?") == 3
