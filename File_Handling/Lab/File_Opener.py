file_path = "text.txt"
try:
    file_path = open(file_path, "r")
    print(file_path)
except FileNotFoundError:
    print("File not found")
