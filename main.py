import sys
from stats import count_words
from stats import count_no_chars
from stats import build_char_list
from stats import print_function

def main():
    print("Usage: python3 main.py <path_to_book>")
    # path = "books/frankenstein.txt" 
    path = sys.argv[1]
    print(print_function(path))

main()

