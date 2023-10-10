def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    print(text)
    print(num_of_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    lines = text.split()
    return len(lines)
    
main()