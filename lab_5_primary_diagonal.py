def sum_primary_diagonal(matrix):
    sum_matrix_diagonal = 0
    for i in range(size):
        for j in range(len(matrix[i])):
            if i == j:
                sum_matrix_diagonal += matrix[i][j]
    return sum_matrix_diagonal


def sum_secondary_diagonal(matrix):
    sum_matrix_secondary_diagonal = 0
    for i in range(size):
        for j in range(len(matrix[i])):
            if i == len(matrix) - 1 - j:
                sum_matrix_secondary_diagonal += matrix[i][j]
    return sum_matrix_secondary_diagonal


size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split(' ')])

print(sum_primary_diagonal(matrix))
print(sum_secondary_diagonal(matrix))
