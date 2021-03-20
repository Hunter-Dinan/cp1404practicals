"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = 0
    while denominator <= 0:
        denominator = int(input("Enter the denominator: "))
        if denominator <= 0:
            print("Denominator cannot be less than or equal to 0, try again.")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# Question 1
# ValueError occurs when any non-integer type is entered

# Question 2
# ZeroDivisionError occurs when the denominator <= 0

