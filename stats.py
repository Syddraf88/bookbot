BOOK_DIR_PATH = "../bookbot/books/"
def get_book_text(book_name):
    
    file_path = BOOK_DIR_PATH + book_name
    with open(file_path) as f:
        contents = f.read()
        return contents

def word_count(book_name):
    book_text = get_book_text(book_name)
    words = book_text.split()
    return len(words)