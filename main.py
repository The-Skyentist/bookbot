from stats import word_count
from stats import character_count
from stats import sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    book_count = word_count(book_text)
    char_count = character_count(book_text)
    char_sort = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for key, value in char_sort.items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()