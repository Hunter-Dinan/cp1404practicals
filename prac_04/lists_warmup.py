numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] == 3
# numbers[-1] == 2
# numbers[3] == 1
# numbers[:-1] == [3, 1, 4, 1, 5, 9]
# numbers[3:4] == 1
# 5 in numbers == True
# 7 in numbers == False
# "3" in numbers == False
# numbers + [6, 5, 3] == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
sliced_numbers = numbers[2:]
print(sliced_numbers)

if 9 in numbers:
    print(numbers)
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")
