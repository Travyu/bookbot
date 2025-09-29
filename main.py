from stats import get_book_text, word_count, character_count, sort_on

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = word_count(book)
    print(f"Found {num_words} total words")
    char_dict = character_count(book)
    # print(character_count(book))
    
    dict_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": num}
            dict_list.append(new_dict)
    

    dict_list.sort(reverse=True, key=sort_on)

    print(*dict_list, sep="\n")
    
main()