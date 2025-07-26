# define  a new funciton 
def get_books_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

# count the words in the book
def count_words(path):
    file_contents = get_books_text(path)
    file_contents_list = file_contents.split()
    return(len(file_contents_list))

# count the number of chars in the book function
def count_no_chars(path):
    file_contents = get_books_text(path)
    file_contents_list = file_contents.split()

    #define a hash list
    seen = {}
    for word in file_contents_list:
        
        for char in word:
            # lower the char 
            curr_char = char.lower()
            if curr_char not in seen:
                seen[curr_char] = 1
            else:
                seen[curr_char] += 1
    return seen

# takes the dict of characters and their counts and 
# returns a sorted list of dict
def sort_on(item):
    # get the dict of chars
    return item["num"]

def build_char_list(path):
    char_dict = count_no_chars(path)
    char_list = [{"char": ch, "num":count} for ch, count in char_dict.items()]
    char_list.sort(reverse = True, key = sort_on)
    return char_list

def print_function(path):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(path)} total words")
    print("--------- Character Count -------")
    for word in build_char_list(path):
        print(f"{word['char']}: {word['num']}")
    


