import os

try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File already deleted!")
