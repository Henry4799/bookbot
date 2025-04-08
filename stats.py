
def word_count(book_text):
    text = book_text
    words = text.split()
    count = len(words)
    return(count)

def character_count(book_text):
    characters = {}
    text = book_text.lower()
    for letter in text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_on(dict_item):
    char = list(dict_item.keys())[0]
    return dict_item[char]

def sort(characters):
    chars_list = []
    for char, count in characters.items():
        chars_list.append({char: count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list