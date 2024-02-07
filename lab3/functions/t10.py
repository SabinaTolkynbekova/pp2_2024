def unique_elements(input_list):
    """Return a new list with unique elements of the input list."""
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9]
print("Original list:", input_list)
unique_list = unique_elements(input_list)
print("List with unique elements:", unique_list)
