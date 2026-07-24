# 1. Count number of vowels in a string.
# 2. Remove duplicate characters.
# 3. Check if string is palindrome.
# 4. Replace all vowels with '*'.
# 5. Check if two strings are anagrams.
# 6. Find all occurrences of a substring.
# 7. Reverse each word in a sentence.
# 8. Find longest word in a sentence.
# 9. Extract digits from a string.
# 10. Remove digits from a string.
# 11. Convert camelCase to snake_case.
# 12. . Count frequency of characters.
# 13. . Keep only alphanumeric characters.
# 14. . Capitalize first letter of each word.
# 15. . Replace multiple spaces with single space.
# 16. . Encode string with ROT13 cipher.
# 17. . Mask a string like a password.
# 18. . Add ordinal suffix to number string.
# 19. . Implement custom trim function.
# 20. . Find common characters in two strings.
# 21. . Convert tab-separated string to list.
# 22. . Count uppercase and lowercase characters.
# 23. . Extract email from text string.
# 24. Count lines in a multi-line string.

# 25. Escape characters in a string.
# 26. Replace multiple substrings with map.
# 27. Parse key-value pairs from string.
# 28. Check for balanced parentheses.
# 29. Remove HTML tags from string.
# 30. Convert numeric string to int safely.
# 31. Count how many words start with a vowel.
# 32. Group words by first character.
# 33. Sort string by characters.
# 34. Remove nth character from a string.
# 35. Remove all whitespaces from string.
# 36.Create a string with your name and print it.
# 37. Get the first character from the string.
# 38. Get the last character from the string.
# 39. Concatenate two strings.
# 40. Repeat a string 3 times.
# 41. Slice the first 5 characters.
# 42. Reverse a string using slicing.
# 43. Check if a substring exists in a string.
# 44. Find the length of a string.
# 45. Convert string to uppercase.
# 46. Convert string to lowercase.
# 47. Capitalize the first letter.
# 48. Convert a string to title case.
# 49.Remove leading spaces using lstrip().
# 50. Remove trailing spaces using rstrip().
# 51. Remove both ends' spaces using strip().

# 52. Replace all spaces with underscores.
# 53. Count how many times a character appears.
# 54. Find index of a character using find().
# 55. Use rfind() to find last occurrence.
# 56.Use index() to find substring position.
# 57.Split a string by spaces.
# 58.Join a list of words into a string.
# 59. Check if string starts with "Hello".
# 60. Check if string ends with "world".
# 61. Check if a string is digit.
# 62. Check if a string is alphabet.
# 63. Check if a string is alphanumeric.
# 64. Get ASCII value of a character.
# 65. Convert ASCII to character.
# 66. Remove punctuation from string.
# 67. Swap case of all characters.
# 68. Count total words in a string.
# 69. Count total sentences in a string.
# 70. Convert string to list of characters.
# 71. Convert list of characters to string.
# 72. Pad string to the left with * to length 10.
# 73. Center align string using center().
# 74. Format string with variables using f-string.
# 75. Use % operator to format a string.


















# 1. Count number of vowels in a string
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

# 2. Remove duplicate characters
def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

# 3. Check if string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# 4. Replace all vowels with '*'
def replace_vowels(s):
    return "".join('*' if ch.lower() in "aeiou" else ch for ch in s)

# 5. Check if two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# 6. Find all occurrences of a substring
def find_occurrences(s, sub):
    return [i for i in range(len(s)) if s.startswith(sub, i)]

# 7. Reverse each word in a sentence
def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

# 8. Find longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 9. Extract digits from a string
def extract_digits(s):
    return "".join(ch for ch in s if ch.isdigit())

# 10. Remove digits from a string
def remove_digits(s):
    return "".join(ch for ch in s if not ch.isdigit())

# 11. Convert camelCase to snake_case
import re
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower()

# 12. Count frequency of characters
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 13. Keep only alphanumeric characters
def keep_alnum(s):
    return "".join(ch for ch in s if ch.isalnum())

# 14. Capitalize first letter of each word
def capitalize_words(s):
    return s.title()

# 15. Replace multiple spaces with single space
def normalize_spaces(s):
    return " ".join(s.split())

# 16. Encode string with ROT13 cipher
import codecs
def rot13(s):
    return codecs.encode(s, 'rot_13')

# 17. Mask a string like a password
def mask_string(s):
    return "*" * len(s)

# 18. Add ordinal suffix to number string
def ordinal_suffix(n):
    n = int(n)
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1:"st",2:"nd",3:"rd"}.get(n%10,"th")
    return str(n) + suffix

# 19. Implement custom trim function
def custom_trim(s):
    return s.strip()

# 20. Find common characters in two strings
def common_chars(s1, s2):
    return "".join(set(s1) & set(s2))

# 21. Convert tab-separated string to list
def tab_to_list(s):
    return s.split("\t")

# 22. Count uppercase and lowercase characters
def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

# 23. Extract email from text string
import re
def extract_email(s):
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", s)

# 24. Count lines in a multi-line string
def count_lines(s):
    return len(s.splitlines())

# 25. Escape characters in a string
def escape_string(s):
    return s.encode('unicode_escape').decode()

# 26. Replace multiple substrings with map
def replace_map(s, mapping):
    for old, new in mapping.items():
        s = s.replace(old, new)
    return s

# 27. Parse key-value pairs from string
def parse_kv(s):
    return dict(item.split("=") for item in s.split(","))

# 28. Check for balanced parentheses
def balanced_parentheses(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack: return False
            stack.pop()
    return not stack

# 29. Remove HTML tags from string
def remove_html(s):
    return re.sub(r"<.*?>", "", s)

# 30. Convert numeric string to int safely
def safe_int(s):
    return int(s) if s.isdigit() else None

# 31. Count how many words start with a vowel
def words_start_vowel(sentence):
    return sum(1 for w in sentence.split() if w[0].lower() in "aeiou")

# 32. Group words by first character
from collections import defaultdict
def group_by_first_char(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)

# 33. Sort string by characters
def sort_string(s):
    return "".join(sorted(s))

# 34. Remove nth character from a string
def remove_nth(s, n):
    return s[:n] + s[n+1:]

# 35. Remove all whitespaces from string
def remove_whitespace(s):
    return "".join(s.split())

# 36. Create a string with your name and print it
name = "GANDRA"
print(name)

# 37. Get the first character from the string
def first_char(s):
    return s[0]

# 38. Get the last character from the string
def last_char(s):
    return s[-1]

# 39. Concatenate two strings
def concat(s1, s2):
    return s1 + s2

# 40. Repeat a string 3 times
def repeat3(s):
    return s * 3

# 41. Slice the first 5 characters
def slice5(s):
    return s[:5]

# 42. Reverse a string using slicing
def reverse_string(s):
    return s[::-1]

# 43. Check if a substring exists in a string
def substring_exists(s, sub):
    return sub in s

# 44. Find the length of a string
def str_length(s):
    return len(s)

# 45. Convert string to uppercase
def to_upper(s):
    return s.upper()

# 46. Convert string to lowercase
def to_lower(s):
    return s.lower()

# 47. Capitalize the first letter
def capitalize_first(s):
    return s.capitalize()

# 48. Convert a string to title case
def to_title(s):
    return s.title()

# 49. Remove leading spaces using lstrip()
def trim_left(s):
    return s.lstrip()

# 50. Remove trailing spaces using rstrip()
def trim_right(s):
    return s.rstrip()

# 51. Remove both ends' spaces using strip()
def trim_both(s):
    return s.strip()

# 52. Replace all spaces with underscores
def spaces_to_underscores(s):
    return s.replace(" ", "_")

# 53. Count how many times a character appears
def count_char(s, ch):
    return s.count(ch)

# 54. Find index of a character using find()
def find_char(s, ch):
    return s.find(ch)

# 55. Use rfind() to find last occurrence
def rfind_char(s, ch):
    return s.rfind(ch)

# 56. Use index() to find substring position
def find_substring(s, sub):
    return s.index(sub)

# 57. Split a string by spaces
def split_spaces(s):
    return s.split()

# 58. Join a list of words into a string
def join_words(words):
    return " ".join(words)

# 59. Check if string starts with "Hello"
def starts_with_hello(s):
    return s.startswith("Hello")

# 60. Check if string ends with "world"
def ends_with_world(s):
    return s.endswith("world")

# 61. Check if a string is digit
def is_digit(s):
    return s.isdigit()

# 62. Check if a string is alphabet
def is_alpha(s):
    return s.isalpha()

# 63. Check if a string is alphanumeric
def is_alnum(s):
    return s.isalnum()

# 64. Get ASCII value of a character
def ascii_value(ch):
    return ord(ch)

# 65. Convert ASCII to character
def char_from_ascii(val):
    return chr(val)

# 66. Remove punctuation from string
import string
def remove_punct(s):
    return "".join(ch for ch in s if ch not in string.punctuation)

# 67. Swap case of all characters
def swap_case(s):
    return s.swapcase()

# 68. Count total words in a string
def count_words(s):
    return len(s.split())

# 69. Count total sentences in a string
def count_sentences(s):
    return s.count(".") + s.count("!") + s.count("?")

# 70. Convert string to list of characters
def string_to_list(s):
    return list(s)



def list_to_string(lst):
    return "".join(lst)


def pad_left(s, length):
    return s.rjust(length, '*')


def center_align(s, width):
    return s.center(width)


def format_with_fstring(name, age):
    return f"My name is {name} and I am {age} years old."


def format_with_percent(name, age):
    return "My name is %s and I am %d years old." % (name, age)