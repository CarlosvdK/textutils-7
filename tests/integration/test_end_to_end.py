import textutils.core as c

def test_full_text_processing_pipeline():
       text = "Red red BLUE"
       normalized = c.normalize_whitespace(text)
       counts = c.word_count(normalized)
       result = c.top_n(counts, 2)
       assert result == [("red", 2), ("blue", 1)]