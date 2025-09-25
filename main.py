def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def word_counter(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
    return word_count

def main():
    total_words = word_counter("/Users/hydena/workspace/github.com/hydenaw/bookbot/books/frankenstein.txt")
    print(total_words)
main()