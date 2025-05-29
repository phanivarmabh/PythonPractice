def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list): # isinstance: If item is nested list then it flatten the list 
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested = [1, [2, 3], [4, [5, 6]], 7]
result = flatten_list(nested)
print(result)