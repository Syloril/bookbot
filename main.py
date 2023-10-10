def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    num_chars = get_char_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End report ---")

def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
main()