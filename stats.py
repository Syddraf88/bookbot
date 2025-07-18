'''
this file contains all of the functions related to data analasys of a selected book

'''
BOOK_DIR_PATH = "../bookbot/books/" #Global Variable to books folder
def get_book_text(book_name): #Book file handler, Reads contents to ""
    
    file_path = BOOK_DIR_PATH + book_name
    with open(file_path) as f:
        contents = f.read()
        return contents

def word_count(book_name): #Counts all words in file, Dependent on get_book_text to handle file
    book_text = get_book_text(book_name)
    words = book_text.split()
    return len(words)

def char_count(book_name): #Counts total occurances of each character in the file
    book_text = get_book_text(book_name)
    lowercase_book_text = book_text.lower()
    characters = {}
    for character in lowercase_book_text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters