
# this is the function that counts the numbers of words      
def num_of_words(word):
    words_list = word.split()
    return len(words_list)


# this function is counting all the characters that are in the book and then returning them all lowercase
def num_of_characters(word): 
    word = word.lower()
    char_count = {}
    for c in word:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count






# This function takes the dictionary of characters and their counts and returns a sorted list of dictionaries
def sorted_list(char_dict):
    sorted_dict = [] # here we create an empty list to store the results
    for char, count in char_dict.items(): # Looping over(character, count) PAIRS in the dictonary.
        if char.isalpha():   # isalpha() is a method that determines if all strings are alphabets
            sorted_dict.append({"char": char, "num": count}) #Add a dict for this char and count 
    sorted_dict.sort(reverse=True, key=lambda item: item["num"]) # sort by 'num' descending. LAMBDA is a tiny function inside a bigger function 
    return sorted_dict
        
    
    