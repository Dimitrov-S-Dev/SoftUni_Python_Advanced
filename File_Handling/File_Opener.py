
try:
    file_path = open("text.txt", "r")
except FileNotFoundError:
    print("File not found")
