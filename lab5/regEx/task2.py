# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# | - either or

import re

word = "abbb abbcabbbabb"

print(re.match("abbb|abb", word))