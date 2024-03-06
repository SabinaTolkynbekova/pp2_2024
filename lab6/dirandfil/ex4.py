import os

filename = input("Enter the path to the text file: ")
if os.path.exists(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for _ in file)
    print(f"Number of lines in the file: {line_count}")
else:
    print(f"Error: File '{filename}' not found.")
