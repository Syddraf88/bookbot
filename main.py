'''
this script is dependant on functions in the stat.py file and must be imported at the top of the script.
to use these functions you must define the book_to_analyze variable in the main function.
and the book must be stored in a relative path that matches "../bookbot/books/"
'''
#BOOK_TO_ANALYZE = "frankenstein.txt"
import sys

from stats import word_count, char_count_report, char_count

def argument_check():
    if len(sys.argv) < 1:
        print("Usage: python3 main.py <path_to_book>")
        sys._ExitCode(1)

def main():
    
    #book_to_analyze = "frankenstein.txt"
    #num_words_found = word_count(book_to_analyze)
    #character_count = char_count_report(book_to_analyze)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_report(f"{sys.argv[1]}")
    
def print_report(book_name):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_name}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_name)} total words")
    print("--------- Character Count -------")
    for item in char_count_report(book_name):
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")
    



main()