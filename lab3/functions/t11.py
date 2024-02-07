def is_palindrome(word):
    """Check if a word or phrase is a palindrome."""
    
    word = word.replace(' ', '').lower()
    
    return word == word[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
