'''
this file contains all of the functions related to data analasys of a selected book

'''
book_name = "frankenstein.txt"
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

def sort_on(d):
    return d["num"]

def char_count_report(book_name): #Refines character count into human readablie report of alpha num list.
    report_data = char_count(book_name)
    sorted_data = []
    scrubbed_data = []
    for ch in report_data:
        scrubbed_data.append({"char": ch, "num": report_data[ch]})
    sorted_data.sort(reverse=True, key=sort_on)
    for item in sorted_data:
        if item["char"].isalpha():
            scrubbed_data.append

            
    return scrubbed_data