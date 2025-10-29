def word_count(text):
    return 2

def top_n(counts, n):
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]