def calculate_running_average(numbers):
    running_sum = 0
    running_average_list = []

    for i, num in enumerate(numbers, start=1):
        running_sum += num
        running_average = running_sum / i
        running_average_list.append(running_average)

    return running_average_list


numbers = [int(x) for x in input("Enter a series of numbers separated by spaces: ").split()]
running_average_result = calculate_running_average(numbers)
print("Running average list:", running_average_result)
