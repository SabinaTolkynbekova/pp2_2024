def reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

input_str = input()
reversed_str = reverse_string(input_str)
print(reversed_str)
