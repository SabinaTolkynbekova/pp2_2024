def spy_game(nums):
    has_007 = False
    zeros_count = 0

    for num in nums:
        if num == 0 and zeros_count == 0:
            zeros_count += 1
        elif num == 0 and zeros_count == 1:
            zeros_count += 1
        elif num == 7 and zeros_count == 2:
            has_007 = True
            break

    return has_007

print(spy_game([1,2,4,0,0,7,5]))   
print(spy_game([1,0,2,4,0,5,7]))   
print(spy_game([1,7,2,0,4,5,0]))   