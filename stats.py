
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