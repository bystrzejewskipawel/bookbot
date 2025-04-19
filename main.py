from stats import get_book_text
from stats import get_char_count
from stats import get_num_words
from stats import sort_dicts
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    d = get_char_count(get_book_text(book_path))
    lst = sort_dicts(d)
    for d in lst:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
main()