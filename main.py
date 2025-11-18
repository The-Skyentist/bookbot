from stats import word_count
from stats import character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    Frank_Path = "books/frankenstein.txt"
    Frank_Book = get_book_text(Frank_Path)
    Frank_Count = word_count(Frank_Book)
    Frank_Char_Count = character_count(Frank_Book)

    print(f"Found {Frank_Count} total words")
    print(Frank_Char_Count)

main()