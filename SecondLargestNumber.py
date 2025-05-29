# def second_largest_num(lst):
#     unique = list(set(lst))
#     unique.sort(reverse=True)
#     return unique[1]

def second_largest_num(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1]

print(second_largest_num([6, 2, 3, 1, 8, 4]))