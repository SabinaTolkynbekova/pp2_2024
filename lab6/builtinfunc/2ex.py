def cnt_upper_lower(string):
    if not string:
        return 0, 0
    upper_cnt = sum(1 for char in string if char.isupper())
    lower_cnt = sum(1 for char in string if char.islower())

    return upper_cnt, lower_cnt


str = input()
upper = cnt_upper_lower(str)
lower = cnt_upper_lower(str)
print("Number of uppercase:", upper)
print("Number of lowercases:", lower)