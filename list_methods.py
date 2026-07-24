# Remove duplicate elements.
# Count the frequency of each element.
# Find the most frequent element.
# Find the least frequent element.
# Check whether a given element exists.
# Find the index of an element without using index().
# Merge two lists.
# Find common elements between two lists.
# Find elements present in the first list but not in the second.
# Rotate a list left by one position.
# Rotate a list right by one position.
# Rotate a list by k positions.
# Sort a list without using sort().
# Check whether a list is sorted.
# Split a list into two equal halves.




# 1. Remove duplicate elements
def remove_duplicates(lst):
    return list(set(lst))

# 2. Count the frequency of each element
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 3. Find the most frequent element
def most_frequent(lst):
    freq = count_frequency(lst)
    return max(freq, key=freq.get)

# 4. Find the least frequent element
def least_frequent(lst):
    freq = count_frequency(lst)
    return min(freq, key=freq.get)

# 5. Check whether a given element exists
def element_exists(lst, element):
    return element in lst

# 6. Find the index of an element without using index()
def find_index(lst, element):
    for i, val in enumerate(lst):
        if val == element:
            return i
    return -1

# 7. Merge two lists
def merge_lists(lst1, lst2):
    return lst1 + lst2

# 8. Find common elements between two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 9. Find elements present in the first list but not in the second
def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

# 10. Rotate a list left by one position
def rotate_left(lst):
    return lst[1:] + lst[:1]

# 11. Rotate a list right by one position
def rotate_right(lst):
    return lst[-1:] + lst[:-1]

# 12. Rotate a list by k positions
def rotate_k(lst, k):
    k = k % len(lst)  # handle k > len(lst)
    return lst[k:] + lst[:k]

# 13. Sort a list without using sort()
def manual_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# 14. Check whether a list is sorted
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# 15. Split a list into two equal halves
def split_list(lst):
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]




