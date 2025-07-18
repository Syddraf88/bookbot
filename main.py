'''
this script is dependant on functions in the stat.py file and must be imported at the top of the script.
to use these functions you must define the book_to_analyze variable in the main function.
and the book must be stored in a relative path that matches "../bookbot/books/"
'''

from stats import word_count, char_count

def main():
    
    book_to_analyze = "frankenstein.txt"
    num_words_found = word_count(book_to_analyze)
    character_count = char_count(book_to_analyze)
    print(F"{num_words_found} words found in the document")
    print(f"{character_count}")


main()