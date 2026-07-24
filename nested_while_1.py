# Create a Python program that uses nested while loops to print a pattern of numbers where the outer loop controls the number of rows, and the inner loop prints the numbers in each row.
# The pattern should have a specific number of rows (e.g., 5 rows) and each row should contain a sequence of ascending numbers starting from 1 (e.g., Row 1: 1, Row 2: 1 2, Row 3: 1 2 3, etc.).
# Ensure that the loop variables are properly initialized and updated to achieve the desired pattern.
# Write a comment at the top of your program explaining the purpose of the nested while loop used in the assignment.
# Test your program with different numbers of rows to verify its functionality




#the purpose of nested while loops in this program is to create a pattern of numbers where the outer loop controls the number of rows, and the inner loop prints a sequence of ascending numbers in each row. The outer loop iterates through each row, while the inner loop generates the numbers for that specific row.
n=0
while n<5:
    m=0
    while m<=n:
        print(m+1, end=' ')
        m+=1
    print()  # Move to the next line after finishing a row
    n+=1
