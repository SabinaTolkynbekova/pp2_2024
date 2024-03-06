import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"the path '{path}' exists.")
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path does not exist.")



path = input("Enter the path:")
print(analyze_path(path))