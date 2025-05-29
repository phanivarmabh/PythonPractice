def largest_smallest_ele(lst):
    largest = smallest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

nums = [1, 22, 4, 56, 7]
big, small = largest_smallest_ele(nums)
print(f"Largest: {big}")
print(f"Smallest: {small}")