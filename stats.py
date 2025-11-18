def word_count(book_text):
    total_words = book_text.split()
    return len(total_words)

def character_count(book_text):
    char_list = list(book_text.lower())
    char_count ={}
    for char in char_list:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
