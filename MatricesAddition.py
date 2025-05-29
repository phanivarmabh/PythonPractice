def add_matrices(A, B):
    result = []
    for i in range(len(A)): # rows
        row = []
        for j in range(len(A[0])): # Columns
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(add_matrices(A, B))  # Output: [[6, 8], [10, 12]]