from stats import character_count, word_counter
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    characters = character_count(file)
    word_count = word_counter(file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")      
    for line in characters:
        print(line)
    print("============= END ===============")
main()
