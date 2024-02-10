def word_frequency(input_string):
    words = input_string.split()
    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

input_str = input("Enter a string: ")
frequency_result = word_frequency(input_str)
print("Word frequency:", frequency_result)
