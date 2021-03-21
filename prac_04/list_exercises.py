numbers = []

for i in range(0, 5):
    number_input = int(input("Number: "))
    numbers.append(number_input)

average = sum(numbers)/5

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(average))
