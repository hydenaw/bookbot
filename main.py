from stats import character_count, word_counter
def main():
    file = "books/frankenstein.txt"
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
