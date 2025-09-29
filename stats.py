def get_book_text(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

def character_count(book):
    character_key = {}
    default_count = 0
    lowercase_book = book.lower()
    for character in lowercase_book:
        character_key.setdefault(character, default_count)
        character_key[character] += 1
    return character_key

def sort_on(dict):
    return dict["num"]
        
def chars_dict_to_sorted_list(char_dict):
    dict_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": num}
            dict_list.append(new_dict)
    

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list        
