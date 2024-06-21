from MatrixProject import *
# from sympy import init_session
# init_session()

# 1 пример несовместная система
# A = sp.Matrix([[4, -3, 2, -1],
#                [3, -2, 1, -3],
#                [5, -3, 1, -8]])
# y = sp.Matrix([[8],
#                [7],
#                [1]])

#2 пример совместная система
# A = sp.Matrix([[1, -1, 2, 0],
#                 [-1, 2, -3, 1],
#                 [0, 5, -1, 1]])
# y = sp.Matrix([[-1],
#                 [4],
#                [3]])
#
# 3 пример
# A = sp.Matrix([[1, 1],
#                 [1, 1]])
#
# y = sp.Matrix([[1],
#                 [1]])

# 4 пример
# A = sp.Matrix([[1, 1],
#                [1, 1]])
# M = sp.Matrix([['a', 'a'],
#                ['a', 'a']])
#
# 4 пример
# A = sp.Matrix([[1, 1],
#                 [2, 2]])
# y = sp.Matrix([[3],
#                 [6]])
#
# A = A + M
# print(A)
#
#  y = sp.Matrix([[1],
#                [1]])
#
#
# A, A_m, A_n = enter_matrix_A()
# y = enter_matrix_y(A_m)
#
# solution_of_matrix(A, y)
#
# doc.append(Math(data=['A = ', pl.Matrix(A)], escape=False))
# pinverse_with_pdf(A)
# doc.generate_pdf("Matrix")
#
#
# orthoproektor_na_obraz(A)
#
# ortoproektor_na_yadro(A)
#
#
# A = Matrix([[1, 1],
#                 [1, 1]])
# y = Matrix([[1],
#                [1]])
# B = Matrix([[0, 0],
#                [0, 0]])
# z = Matrix([[1],
#               [3]])
#
# norm_sol = norm_related_pseudo_sol(A, y, B, z)
#
# reg_sol = reg_sol(A, y, B, z)
#
#
# from MatrixProject import *
#
#
# norm_sol = norm_related_pseudo_sol(A, y, B, z)
#
# reg_sol = reg_sol(A, y, B, z)
#
# n = symbols('n')
# parametrization_reg_sol(reg, n ** 2, 1 / n, 1 / n ** 4)
#
# Matrix(param)
#
#
# lim = lim_param_resh(param)
# Matrix(lim)
# # G = regul_resh_with_print(A, y, B, z)
#
# n = sp.symbols('n')
#
# G = parametrization_reg_resh(G, 1/n, n**2, 1/(n*4))

# sp.pprint(G)
# A = sp.Matrix([[1, 0, 0, 0],
#                 [0, e, 0, 0],
#                [0, 0, 1, 0],
#                [0, 0, 0, 0]])
# y = sp.Matrix([[1],
#                [1],
#                [1],
#                [1]])
# B = sp.Matrix([[0, 0, 0, 0],
#                 [0, 1, 0, 0],
#                [0, 0, 0, 0],
#                [0, 0, 0, 1]])
# z = sp.Matrix([[1],
#               [2],
#                [3],
#                [4]])


# norm_svyazanoe_pseudoresh(A, y, B, z)

# orthoproektor_na_yadro_sostavnogo_operatora_with_pdf(A, A)

# orthoproektor_na_yadro_with_pdf(B)

# doc.generate_pdf('test')


# from MatrixProject import *
#
# e = symbols('e')
# n = symbols('n')
# r = n**2
# a = 1/n
# e = 1/n**4
#
# A = Matrix([[1+e, 1, 1],
#             [1, 1, 1],
#             [1, 1, 1]])
# y = Matrix([[2],
#             [3],
#             [5]])
# B = Matrix([[1, 1, 1],
#             [1, 1, 1],
#             [0, 0, e]])
# z = Matrix([[1],
#             [2],
#             [3]])
#
# reg_sol(A, y, B, z, r, a)

# parametrization_reg_sol(reg, n**2, 1/n, 1/n**4)

# A = Matrix([[1+e, 1, 1],
#             [1, 1, 1],
#             [1, 1, 1]])
# y = Matrix([[2],
#             [3],
#             [5]])
# B = Matrix([[1, 1, 1],
#             [1, 1, 1],
#             [0, 0, e]])
#             [3]])
# z = Matrix([[1],
#             [2],

# e = symbols('e')
#
# A = Matrix([[1, 3],
#             [2, 6],
#             [3, 9],
#             [4, 12]])
# y = Matrix([[1],
#             [1],
#             [1],
#             [1]])
# B = Matrix([[0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]])
# z = Matrix([[0],
#             [0],
#             [0],
#             [0]])

from MatrixProject import *

# A = Matrix([[1, 1],
#             [1, 1]])
# y = Matrix([[1],
#             [1]])
# B = Matrix([[0, 0],
#             [0, 0]])
# z = Matrix([[1],
#             [3]])

norm_related_pseudo_sol(A, y, B, z)

reg_sol(A, y, B, z)

e = symbols('e')

A = Matrix([[1, 1+e],
            [1, 1]])
y = Matrix([[1],
            [1]])
B = Matrix([[e, 0],
            [0, 0]])
z = Matrix([[1],
            [3]])
#
# norm_related_pseudo_sol(A, y, B, z)
#
# reg_sol(A, y, B, z)