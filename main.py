from stats import (
    get_book_text, 
    word_count, 
    character_count, 
    chars_dict_to_sorted_list,
    )

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = word_count(book)
    char_dict = character_count(book) 
    print_report(book_path, num_words, char_dict)
    

def print_report(book_path, num_words, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in chars_dict_to_sorted_list(char_dict):
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

main()