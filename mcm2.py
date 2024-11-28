import numpy as np

def matrix_chain_order(dims):
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
                    split[i][j] = k
    return dp[0][n - 1], split

def print_optimal_parenthesization(split, i, j):
    if i == j:
        print(f"A{i + 1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(split, i, split[i][j])
        print_optimal_parenthesization(split, split[i][j] + 1, j)
        print(")", end="")

A1 = np.array([[30, 32, 33, 31, 30, 29, 28]])
A2 = np.array([[10], [12], [15], [14], [13], [12], [11]])
A3 = np.array([[75, 70, 60, 65, 72, 78, 80]])

dims = [1, 7, 1, 7]

min_cost, split = matrix_chain_order(dims)

print(f"Minimum multiplication cost: {min_cost}")
print("Optimal parenthesization: ", end="")
print_optimal_parenthesization(split, 0, len(dims) - 2)

def matrix_multiply(A, B):
    return np.dot(A, B)

result1 = matrix_multiply(A1, A2)
final_result = matrix_multiply(result1, A3)

print()
print("Final result of matrix multiplication:")
print(final_result)
