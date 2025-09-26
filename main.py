from stats import word_counter
def main():
    total_words = word_counter("/Users/hydena/workspace/github.com/hydenaw/bookbot/books/frankenstein.txt")
    print(f"Found {total_words} total words")
main()