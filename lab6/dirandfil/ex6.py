import os

path_to_file = '\Users\User\Desktop\pp2_2024\lab6\dirandfil'

os.mkdir(path_to_file)
start_char = 'A'
end_char = 'Z'

for i in range(ord(start_char), ord(end_char) + 1):
    file = open(f"{path_to_file}{i}.txt", "w")
    file.write(f"You're in {file.name}")
    file.close()


