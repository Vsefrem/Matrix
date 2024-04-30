from MatrixProject import *

# 1 пример
# A_m = 3
# A_n = 4
# A = sp.Matrix([[1, -1, 2, 0],
#                [-1, 2, -3, 1],
#                [0, 5, -1, 1]])
# y = sp.Matrix([[-1],
#                [4],
#                [3]])


# 2 пример
# A_m = 3
# A_n = 4
# A = sp.Matrix([[4, -3, 2, -1],
#                [3, -2, 1, -3],
#                [5, -3, 1, -8]])
# y = sp.Matrix([[8],
#                [7],
#                [1]])

# 3 пример
A_m = 3
A_n = 3
A = sp.Matrix([[1, 0, 0],
               [0, 1, 0],
               [0, 0, 0]])

y = sp.Matrix([[10],
               [1],
               [1]])


# A, A_m, A_n = enter_matrix_A()
# y = enter_matrix_y(A_m)
solution_of_matrix(A, y, A_m, A_n)