# Implement a Python function clean_string that takes a string as input, removes leading and trailing whitespaces, and converts it to lowercase.
# Write a Python function extract_substring that takes two parameters: a string and a starting index. This function should return the substring from the starting index to the end of the string.
# Create a function replace_vowels that replaces all vowels in a given string with '*'.
# Use Python's built-in string method to split a given string into a list of words, assuming words are separated by spaces.
# Demonstrate the use of the join() method to concatenate elements of a list into a single string, with each element separated by a comma.
# Test each function with sample inputs and verify the outputs match the expected results.




def clean_string(input):
    return input.strip().lower()

def extract_substring(input, start_index):
    return input[start_index:]

def replace_vowels(input):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        input = input.replace(vowel, "*")
    return input

def split_into_words(input):
    return input.split()

def join_with_comma(input_list):
    return ", ".join(input_list)




