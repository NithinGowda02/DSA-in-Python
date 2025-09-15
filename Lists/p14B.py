# Transpose of Matrix.

A = [[1, 2, 3],
     [4, 5, 6]]

transpose = []
for i in range(len(A[0])):
    rows = []
    for j in range(len(A)):
        rows.append(A[j][i])
    transpose.append(rows) 
print("Transpose >> ", transpose)       