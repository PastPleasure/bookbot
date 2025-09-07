from stats import get_num_words
from stats import charcount
from stats import helper_key
from stats import sorted_charcount
import sys


def get_book_text(file_path):
    with open(file_path) as f:
              return f.read()
    

def main():
       if len(sys.argv) < 2:
              print("Usage: python3 main.py <path_to_book>")
              sys.exit(1)
       else:
              book_path = sys.argv[1]
       book_text = get_book_text(book_path)
       print("============ BOOKBOT ============")
       print(f"Analyzing book found at {book_path}")
       print("----------- Word Count ----------")
       print(f"Found {get_num_words(book_text)} total words")
       print("--------- Character Count -------")
       sorted = sorted_charcount(charcount(book_text))
       for c in sorted:
              print(f"{c['char']}: {c['num']}")
       print("============= END ===============")
       


main()
