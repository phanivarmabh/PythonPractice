def list_differences(lst1, lst2):
    # result = []
    # for ele in lst1:
    #     if ele not in lst2 and ele not in result:
    #         result.append(ele)
    # for ele in lst2:
    #     if ele not in lst1 and ele not in result:
    #         result.append(ele)
    # return result
    return list(set(lst1) - set(lst2))

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

print(list_differences(lst1, lst2))