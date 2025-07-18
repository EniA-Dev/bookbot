from stats import get_num_words, character_counter, sorted_characters
import re
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
   

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

book_text = get_book_text(filepath)
num_of_words = get_num_words(book_text)
sorted_chars = sorted_characters(book_text)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")
main()
