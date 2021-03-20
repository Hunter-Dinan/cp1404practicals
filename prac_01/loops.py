# Original loop: odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Loop a: count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Loop b: count down from 20 to 1
for i in range(0, 20, 1):
    print(20-i, end=' ')
print()

# Loop c: print number of stars from input
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    print('*', end=' ')
print()

# Loop d: print lines of increasing stars
for i in range(1, number_of_stars+1):
    for j in range(1, i+1):
        if j == i:
            print('*')
        else:
            print('*', end=' ')