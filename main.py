from stats import get_book_text, word_count, character_count, sort_on, chars_dict_to_sorted_list

def main():
    print("============ BOOKBOT ============")
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")
    book = get_book_text(book_path)
    num_words = word_count(book)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_dict = character_count(book) 
    print("--------- Character Count -------")
    for character in chars_dict_to_sorted_list(char_dict):
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

    
main()