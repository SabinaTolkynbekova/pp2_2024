import os

def list_directories_files(path):
    print("Directories and Files in the specified path:")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"Directory: {item}")
        else:
            print(f"File: {item}")

def list_all_directories_files(path):
    print("\nAll Directories and Files including subdirectories:")
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        for file_name in files:
            print(f"File: {os.path.join(root, file_name)}")

if __name__ == "__main__":
    path = input("Enter the path: ")

    print("\nListing directories and files:")
    list_directories_files(path)

    print("\nListing all directories and files:")
    list_all_directories_files(path)
