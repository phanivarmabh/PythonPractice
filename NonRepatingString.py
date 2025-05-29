def nonrepeating_string(s):
    freq = {}
    for x in s:
        freq[x] = freq.get(x,0)+1
    
    for i in s:
        if freq[i] == 1:
            return i
    return -1

print(nonrepeating_string("leetcode"))