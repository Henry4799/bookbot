from stats import word_count
from stats import character_count

file_path = ("")
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    count = word_count(book_text)
    print(f"{count} words found in the document")

    char_count = character_count(book_text)
    print(char_count)

main()