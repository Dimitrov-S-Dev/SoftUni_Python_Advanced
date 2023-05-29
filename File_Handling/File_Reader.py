file_path = "./numbers.txt"
numbers = 0
file = open(file_path)
for line in file:
    numbers += int(line.strip("\n"))

print(numbers)
