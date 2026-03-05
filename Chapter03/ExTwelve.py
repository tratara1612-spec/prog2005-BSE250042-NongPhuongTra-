def add_matrices(A, B, m, n):
    result = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
    return result
