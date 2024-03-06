lst = ["apple", "banana", "kiwi"]
file = open("1.txt", "w")
for item in lst:
    file.write(str(item)+'\n')
file.close()