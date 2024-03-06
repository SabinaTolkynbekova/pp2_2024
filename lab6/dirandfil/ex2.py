import os

def check_path_access(path):
    if os.access(path, os.F_OK):
        print(f"Path '{path}' exists.") 
        print(f"Path '{path}' is {'readible' if os.access(path,os.R_OK) else 'not readible'}.")
        print(f"Path '{path}' is {'writable' if os.access(path,os.W_OK) else 'not writable'}.")
        print(f"Path '{path}' is {'executable' if os.access(path,os.EX_OK) else 'not executable'}.")
    else:
        print("Path does not exists.")

path = input("Enter the path:")
check_path_access(path)