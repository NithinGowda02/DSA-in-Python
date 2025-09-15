# Add two Matrices

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

result = []
for i in range(len(A)):
    rows = []
    for j in range(len(A[0])):
        rows.append(A[i][j] + B[i][j])
    result.append(rows)    
print("Final Result >> ",result)    