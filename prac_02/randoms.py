# What did you see on Line 1?
# Line 1 prints a random integer that is >= 5 and <= 20
# Smallest number = 5
# Largest number = 20

# What did you see on Line 2?
# Line 2 prints a random integer that starts at 3 and ends at 10 with a step of 2 (same as range, largest value is 9)
# This produces all odd numbers
# Smallest = 3
# Largest = 9
# Line 2 could not have produced a 4 as it was using a step of 2 starting at 3

# What did you see on Line 3?
# Line 3 prints a random floating point number that is >= 2.5 and <= 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive
import random
print(random.randint(1, 100))
