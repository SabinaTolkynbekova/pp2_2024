import re
word = "Roses are red_and_violets are blue"
print(re.findall(r'[a-z]+_[a-z]+',word))