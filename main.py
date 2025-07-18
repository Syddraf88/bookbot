from stats import word_count

def main():
    
    book_to_analyze = "frankenstein.txt"
    num_words_found = word_count(book_to_analyze)
    print(F"{num_words_found} words found in the document")


main()