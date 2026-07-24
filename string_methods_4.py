# Generate a function to check whether a given string contains only alphabets.
# Create a method to verify if a string consists solely of digits.
# Develop a function to determine if a string is alphanumeric.
# Write a function that capitalizes the first letter of every word in a sentence.
# Implement a method to count the number of words in a given sentence.
# Design a function to remove all vowels from a specified string.
# Construct a function to check whether a given string is a palindrome.
# Develop a method to replace multiple spaces in a string with a single space.
# Create a function to convert a sentence into camelCase.
# Write a function to convert a sentence into snake_case









def alphabets(input):
    return input.isalpha()


def digit(input):
    return input.isdigit()


def alphanumeric(input):
    return input.isalnum()




def capitalize_words(input):
    return input.title()


def count_words(input):
    return len(input.split())


def remove_vowels(input):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        input = input.replace(vowel, "")
    return input


def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def replace_multiple_spaces(s):
    return s.replace("  ", " ")

def to_camel_case(s):
    words = s.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def to_snake_case(s):
    return s.replace(" ", "_").lower()