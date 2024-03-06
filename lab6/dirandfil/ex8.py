import os
path = input("Enter the path of the file delete: ")

if os.path.exits(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"File '{path}' has been deleted successfully.")
    else: 
        print(f"Error: You don't have write access to '{path}'.")
else:
    print(f"Error: File '{path}' does not exist.")