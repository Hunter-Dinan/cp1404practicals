NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

out_file = open(NAME_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open(NAME_FILE, 'r')
input_name = in_file.read().strip()
in_file.close()
print("Your name is {}".format(input_name))

result = 0
numbers_file = open(NUMBER_FILE, 'r')
for i in range(0, 2):
    number = int(numbers_file.readline())
    result += number
numbers_file.close()
print("Result of first two numbers: {}".format(result))

all_lines_result = 0
numbers_file = open(NUMBER_FILE, 'r')
for line in numbers_file:
    if line != '':
        new_number = int(line)
        all_lines_result += new_number
numbers_file.close()
print("Result of all numbers: {}".format(all_lines_result))
