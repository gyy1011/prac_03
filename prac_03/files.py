# Task 1

name = input("Enter your name: ")

out_file = open("name.txt", "w")

print(name, file=out_file)

out_file.close()

# Task 2

in_file = open("name.txt", "r")

name = in_file.read().strip()

in_file.close()

print("Your name is", name)
# Task 3

in_file = open("numbers.txt", "r")

number1 = int(in_file.readline())

number2 = int(in_file.readline())

in_file.close()
print(number1 + number2)
# Task 4

total_file = open("numbers.txt", "r")

total = 0

for line in total_file:

    total += int(line)

print(total)

total_file.close()