import numpy as np
from numpy.linalg import norm
from math import isclose

import itertools

x = np.array([[1, 0], [2, 1], [10, 5]])
y = np.array([[2, 0, 0], [0, 0, 1]])

# print(np.shape(x))
# print(np.shape(x)[0])
# print(len(x[0]))
# print(np.shape(y[1]))

# for k in range(0, np.shape(y)[1]):
#     print(y[k])

# print(np.shape(y)[1])
# for i in range(0, np.shape(x)[0]):
#     for j in range(0, len(x[0])):
#         for k in range(0, np.shape(y)[1]):
#             # print(x[i][j])
#             a = y[i][k]
#             print(a)

# for i in range(0, np.shape(x)[0]):
#     for j in range(0, len(x[0])):
#         print(x[i][j])

# print(len(y[1]))
# for i in range(0, np.shape(y)[1]):
#     # for k in range(0, len(y[1])):
#     #     print(y[i][k])

# print(np.shape(y))
#
# for i in range(0, np.shape(y)[0]):
#     print(i)

# for i in range(0, np.shape(y)[1]):
#     for k in range(0, np.shape(y)[0]):
#         print(y[k][i])

# for i in range(0, np.shape(x)[0]):
#     for p in range(0, np.shape(x)[1]):
#         for k in range(0, np.shape(y)[0]):
#             print(f'x{[i][p]}', x[i][p])
#             # print('y', y[k][i])
#             # print(x[i][p] * y[p][i])

# for i in range(0, np.shape(x)[0]):
#     for p in range(0, np.shape(x)[1]):
#         print(f'x{i}{p}', x[i][p])

# print(len(x))
# print(len(y))
# print(np.shape(y)[1])


# sum = 0
# matrix = []
# for i in range(0, np.shape(x)[0]):
#     for p in range(0, np.shape(y)[0]):
#         for j in range(0, np.shape(x)[0]):
#             print(f'x{i}{p}', x[i][p])
#             print(f'y{p}{j}', y[p][j])
#             sum += x[i][p] * y[p][j]
#             matrix.append(sum)
#             print('summ =', sum)
#         sum = 0
#         print(matrix)
#         #     # print('y', y[k][i])
#         #     # print(x[i][p] * y[p][i])

# sum = 0
# matrix = []
# for i in range(0, np.shape(x)[0]):
#     for j in range(0, np.shape(x)[0]):
#         for p in range(0, np.shape(y)[0]):
#             # print(f'x{i}{p}', x[i][p])
#             # print(f'y{p}{j}', y[p][j])
#             sum += x[i][p] * y[p][j]
#             # print('summ =', sum)
#         matrix.append(sum)
#         sum = 0
# matrix = np.array(matrix)
# matrix = matrix.reshape(np.shape(x)[0], np.shape(y)[1])
# print(matrix)
#         #     # print('y', y[k][i])
#         #     # print(x[i][p] * y[p][i])




# def dot_simple(A, B):
#     # try:
#     #     len(A[0]) = len(B[0]):
#     #         raise ValueError("Error")
#     # except:
#     #     print('False')
#
#     # try:
#     #     # np.shape(A)[0] = np.shape(B)[0]:
#     #         raise ValueError("Error")
#     # except:
#     #     print('\n km of the last day should be bigger than ')
#
#     sum = 0
#     matrix = []
#     for i in range(0, np.shape(A)[0]):
#         for j in range(0, np.shape(A)[0]):
#             for p in range(0, np.shape(B)[0]):
#             # print(f'x{i}{p}', x[i][p])
#             # print(f'y{p}{j}', y[p][j])
#                 sum += A[i][p] * B[p][j]
#             # print('summ =', sum)
#         matrix.append(sum)
#         sum = 0
#     matrix = np.array(matrix)
#     matrix = matrix.reshape(np.shape(A)[0], np.shape(B)[1])
#     return matrix
#
#
# A = np.array([[4, 1], [5, -2], [2, 3]])
#
# print(dot_simple(A, A.T))

# def dot_simple(A, B):
#   sum = 0
#   matrix = []
#
#   for i in range(0, np.shape(A)[0]):
#     for j in range(0, np.shape(A)[0]):
#        for p in range(0, np.shape(B)[0]):
#             # print(f'x{i}{p}', x[i][p])
#             # print(f'y{p}{j}', y[p][j])
#             sum += A[i][p] * B[p][j]
#             # print('summ =', sum)
#        matrix.append(sum)
#        sum = 0
#   matrix = np.array(matrix)
#   matrix = matrix.reshape(np.shape(A)[0], np.shape(B)[1])
#   return matrix
#
# A = np.array([[4, 1], [5, -2], [2, 3]])
#
# print(dot_simple(A, A.T))

def dot_simple(A, B):
    try:
        # print(np.shape(A))
        # print(np.shape(B))

        print('A[1] = ',np.shape(A)[1])
        print('B[0] = ', np.shape(B)[0])

        if (np.shape(A)[1] != np.shape(B)[0]):
            raise ValueError('Error')
    except:
        return False

    sum = 0
    matrix = []

    for i in range(0, np.shape(A)[0]):
        for j in range(0, np.shape(B)[1]):
            for p in range(0, np.shape(B)[0]):
                # print(f'x{i}{p}', x[i][p])
                # print(f'y{p}{j}', y[p][j])
                sum += A[i][p] * B[p][j]
            matrix.append(sum)
            sum = 0
    matrix = np.array(matrix)
    # print(matrix)
    matrix = matrix.reshape(np.shape(A)[0], np.shape(B)[1])
    return matrix

# A = np.array([[4, 1], [5, -2], [2, 3]])
# print(dot_simple(A, A.T))
# print(dot_simple(A.T, A))

# z = np.empty((2, 5))
# c = np.empty((5, 3))

# z = np.ones((1, 3))
# c = np.ones((3, 2))
#
# print(dot_simple(z, c))
# print(dot_simple(c, z))

# print(dot_simple(x, y))

A = np.empty((2, 5))
B = np.empty((5, 3))

print(dot_simple(A, B))