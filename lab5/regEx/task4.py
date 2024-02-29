import re
word = "Roses are red, violets are blue"
print(re.findall(r'[A-Z]+[a-z]+',word))