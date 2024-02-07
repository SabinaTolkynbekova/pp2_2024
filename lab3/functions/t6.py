def reverse_sentence(input_string):
    words = input_string.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


user_string = input("Enter a sentence: ")

reversed_result = reverse_sentence(user_string)
print("Reversed sentence:", reversed_result)
