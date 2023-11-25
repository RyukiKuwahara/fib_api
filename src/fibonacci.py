def calc_dot(matrix_x, matrix_y):
    matrix_z = [[0, 0],
                [0, 0]]
    for i in range(len(matrix_x)):
        for j in range(len(matrix_y[0])):
            for k in range(len(matrix_y)):
                matrix_z[i][j] += matrix_x[i][k] * matrix_y[k][j]
    return matrix_z


def matrix_power(n):
    if n == 1:
        return [[1, 1],
                [1, 0]]
    
    if n % 2 == 0:
        matrix_x = [[1, 0],
                    [0, 1]]
    else:
        matrix_x = [[1, 1],
                    [1, 0]]
    matrix_y = matrix_power(n // 2)
    matrix_x = calc_dot(matrix_x, matrix_y)
    matrix_x = calc_dot(matrix_x, matrix_y)
    return matrix_x

def calculate_fibonacci(n):
    matrix_a = matrix_power(n)
    matrix_b = [[1],
                [0]]
    matrix_a = calc_dot(matrix_a, matrix_b)
    return matrix_a[1][0]


    