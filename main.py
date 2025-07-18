BOOK_DIR_PATH = "../bookbot/books/"

def get_book_text(book_name):
    #file_path = "/home/matt/projects/github/Syddraf88/bookbot/bookbot/books/frankenstein.txt"
    file_path = BOOK_DIR_PATH + book_name
    with open(file_path) as f:
        contents = f.read()
        return contents

""" def word_count(file_path):
    with open(file_path) as f:
        book = f.read()
        word_list = book.split()
        count = len(word_list)
        return f"{count} words found in the document" """

def word_count(book_name):
    book_text = get_book_text(book_name)
    words = book_text.split()
    return len(words)
    
    


def main():
    #get_book_text("../bookbot/books/frankenstein.txt")
    book_to_analyze = "frankenstein.txt"
    num_words_found = word_count(book_to_analyze)
    print(F"{num_words_found} words found in the document")


main()