def get_book_text(file_path):
    contents = ""
    with open(file_path) as f:
        contents = f.read()
    return contents

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_num_words():
    word_count = get_word_count(get_book_text("books/frankenstein.txt"))
    return word_count

def get_char_count(book_text):
    char_count = {}
    for char in book_text:
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dicts(dict):
    dictonaries = []
    for key in dict:
        if key.isalpha():
            temp_dict = {}
            temp_dict["char"] = key
            temp_dict["num"] = dict[key]
            dictonaries.append(temp_dict)
    dictonaries.sort(reverse=True, key=sort_on)
    return dictonaries