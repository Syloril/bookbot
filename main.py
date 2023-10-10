def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_word_count(text)
    number_for_letter = get_letter_count(text)
    print(num_of_words)
    print(number_for_letter)

def get_word_count(text):
    lines = text.split()
    return len(lines)

def get_letter_count(text):
    letters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
main()