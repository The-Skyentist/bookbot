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

def sort_dict(character_count):
    char_sort_list = sorted(character_count.items(), key = lambda x: x[1], reverse = True)
    char_sort = dict(char_sort_list)
    return char_sort
