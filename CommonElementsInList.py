list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# def common_list(list1, list2):
#     return list(set(list1) & set(list2))

def common_list(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

print(common_list(list1, list2))