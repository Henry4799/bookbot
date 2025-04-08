from stats import word_count
from stats import character_count
from stats import sort
file_path = ("")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    book_text = get_book_text(file_path)
    count = word_count(book_text)
    char_count = character_count(book_text)
    sorted_chars = sort(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = list(char_dict.keys())[0]
        if char.isalpha():
            count = char_dict[char]
            print(f"{char}: {count}")

    print("============= END ===============")

main()