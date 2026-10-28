from collections import Counter

def first_non_repeating(text):
    counts = Counter(text)

    for char in text:
        if counts[char] == 1:
            return char

    return None