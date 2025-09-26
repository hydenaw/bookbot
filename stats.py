def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
    return word_count

def character_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        char_counts = {}
        for char in file_contents:
            char = char.lower()
            char_counts[char] = char_counts.get(char, 0) +1
    return char_counts