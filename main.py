
import sys
from stats import num_of_words
from stats import num_of_characters
from stats import sorted_list


def get_book_text(path_to_file): # defining a function to get text from a file, taking the files path 
    with open(path_to_file) as f: # opens the file specified by 'path_to_file' and assigning it to f
        file_contents = f.read() # reads the entire content of the file 'f' into 'file_contents' 
    return file_contents #return the read content string
       
       

           
        
def main(): # defining the main function where the programs logic resides 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    
    book_contents = get_book_text(book_path) # calls get_book_text functon above with the relative path to the book and it stores the result
    num_words = num_of_words(book_contents)
    print(f"Found {num_words} total words") #prints the stored book contents to the console
    character_dict = num_of_characters(book_contents)
    print(character_dict)
    sorted_chars = sorted_list(character_dict)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    
main() # calls the main function to start program execution.


# "../books/frankenstein.txt"

    
    
