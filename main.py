def get_book_text(file_path):
    #file_path = "/home/matt/projects/github/Syddraf88/bookbot/bookbot/books/frankenstein.txt"
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    print(get_book_text("../bookbot/books/frankenstein.txt"))

main()