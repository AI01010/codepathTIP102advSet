# p1 transpose matrix
# transpose all rows in m*n 2D integer matrix to columns across its diagonal
# cases: m*m, n*m, non-int input, empty list, assume no jagged matrices

# matrix[][]
# (i,j) <=> (j,i) in Transpose
# chek lenght/size of matrix (m*n) create a new, empty (n*m) matrix 
# go row by row on original matrix and make it a col in the new matrix
# old[i][j] --> new[j][i] 

def transpose(matrix):
    m = len(matrix)
    
    if m < 0:
        return
    
    n = len(matrix[0])

    newMatrix = [[0 for x in range(m)] for x in  range(n)]

    for i in range(m):
        for j in range(n):
            newMatrix[j][i] = matrix[i][j]
            
    print(newMatrix)
    return newMatrix
    


matrix = [[1]]
transpose(matrix)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose(matrix)

