from stats import get_book_text, word_count, character_count

def main():
    book_path = "books/frankenstein.txt"
    num_words = word_count(get_book_text(book_path))
    print(f"Found {num_words} total words")
    print(character_count(get_book_text(book_path)))
    
    
main()