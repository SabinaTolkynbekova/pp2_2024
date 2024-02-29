import re

# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# . - any symbol
# ^ - matches only at the beginning of the string
# $ - matches only at the end of the string
txt = input()
#with open("row.txt", encoding="utf-8") as file:
# word = file.read()
print(re.findall("a+.b",txt))