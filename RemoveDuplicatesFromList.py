def remove_duplicates(lst):
    unq = []
    for num in lst:
        if num not in unq:
            unq.append(num)
    return unq

nums = [5, 3, 2, 6, 3, 4, 5]
unq_nums = remove_duplicates(nums)
print(unq_nums)