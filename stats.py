def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
    return word_count

def sort_on(item):
    return item[1]

import string

def character_count(filepath):
    allowed_letters = {
        'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'm', 'u', 'c', 'f',
        'y', 'w', 'p', 'g', 'b', 'v', 'k', 'x', 'j', 'q', 'z', 'æ', 'â', 'ê', 'ë', 'ô'
    }
    
    with open(filepath) as f:
        file_contents = f.read()
        char_counts = {}
        for char in file_contents:
            char = char.lower()
            if char in allowed_letters:
                char_counts[char] = char_counts.get(char, 0) + 1
                
    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    formatted = [f"{char}: {count}" for char, count in sorted_counts]
    return formatted
