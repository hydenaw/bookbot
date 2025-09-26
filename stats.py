def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
    return word_count