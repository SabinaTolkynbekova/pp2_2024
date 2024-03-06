import os
source_filename = input("Enter the path of the source file:")
destination_filename = input("Enter the path of the destination file:")

source_file = open(source_filename, 'r')
destination_file = open(destination_filename, 'w')

for line in source_file:
    destination_file.write(line)

print(f"Contents of '{source_filename}' copied to '{destination_filename}' successfully.")
source_file.close()
destination_file.close()
