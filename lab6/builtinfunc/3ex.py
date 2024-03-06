def is_palindrome(s):
    s = s.replace(" ", "").lower()
    reversed_s = ''.join(reversed(s))
    return s == reversed_s 

string = input()
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
