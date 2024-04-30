# coding: utf-8
from math import sqrt

import latexcompiler
import sympy as sp
from pdflatex import pdflatex
from pylatex import Document, Math, Package, Center, Section
from pylatex.utils import rm_temp_dir, NoEscape
import pylatex as pl


sp.init_printing(use_unicode=False)

rm_temp_dir()
doc = Document(documentclass='article', document_options=None, fontenc=['T2A', 'T1'], lmodern=None, textcomp=None,
               page_numbers=None, indent=True, data=None)
doc.packages.add(Package('babel', options=['english', 'russian']))
doc.packages.add(Package('substitutefont'))
doc.preamble.append(NoEscape(r'\substitutefont {T2A} {/familydefault} {Tempora-TLF}'))



def pinverse(mat):
    # if mat_m == mat.rank():
    print("Строки матрицы C л.н. => матрица CC^T обратима.")
    doc.append('Строки матрицы ')
    doc.append(Math(inline=True, data=['C'], escape=False))
    doc.append('\xa0линейно независимы.')
    doc.append('\nСледовательно, матрица ')
    doc.append(Math(inline=True, data=['CC^T'], escape=False))
    doc.append('\xa0обратима.')
    print("Найдем псевдообратную матрицу по формуле C⁺ = C^T (CC^T)⁻¹:")
    doc.append('\nНайдем псевдообратную матрицу по формуле ')
    doc.append(Math(inline=True, data=['C^+ = C^T(CC^T)^{-1}'], escape=False))
    mat = mat.T * (mat * mat.T).inv()
    print("C⁺: ")
    sp.pprint(mat)
    doc.append(Math(data=['C^+ = ', pl.Matrix(mat)], escape=False))
    return mat
    # else:
    #     print("Найдем псевдообратную матрицу по формуле " + sym + "⁺ = (" + sym + sym + "^T)⁻¹ " + sym + "^T :")
    #     doc.append('Найдем псевдообратную матрицу по формуле ' + sym + '⁺ = (' + sym + sym + '^T)⁻¹ ' + sym + '^T :')
    #     mat = (mat * mat.T).inv() * mat.T
    #     print(sym + "⁺: ")
    #     sp.pprint(mat)
    #     doc.append(Math(data=[str(sym) + '⁺: ', pl.Matrix(mat)]))
    #     return mat

def sovmestnost_check(mat, mat_pinv, column):
    print("Проверим уравнение на совместность.")
    print("Оно должно довлетворять условию AA⁺y = y")
    doc.append('Проверим уравнение на совместность.')
    doc.append('Оно должно довлетворять условию: ')
    doc.append(Math(data=["AA^+y = y"], escape=False))
    if mat * mat_pinv * column == column:
        doc.append(Math(data=[pl.Matrix(mat * mat_pinv * column), ' = ', pl.Matrix(column)], escape=False))
        return True
    else:
        doc.append(Math(data=[pl.Matrix(mat * mat_pinv * column), r'\neq', pl.Matrix(column)], escape=False))
        return False

def enter_matrix_A():
    print("Ax=y")
    print("Введите количество строк матрицы A:")
    A_m = int(input())
    print("Введите количество столбцов матрицы A:")
    A_n = int(input())
    A = sp.Matrix.zeros(A_m, A_n)
    print("Заполнение матрицы A размера ", A_m, "x", A_n, ":", sep='')
    for i in range(A_m):
        for j in range(A_n):
            print("A[", i + 1, ", ", j + 1, "]: ", sep='', end="")
            temp = input()
            if temp.isnumeric():
                A[i, j] = float(temp)
            else:
                A[i, j] = temp
    return A, A_m, A_n

def enter_matrix_y(A_m):
    print("Заполнение вектора y длины ", A_m, ": ", end="")
    y = sp.Matrix.zeros(A_m, 1)
    for i in range(A_m):
        print("y[", i + 1, "]: ", sep='', end="")
        temp = input()
        if temp.isnumeric():
            y[i] = float(temp)
        else:
            y[i] = temp
    return y

def solution_of_matrix(A, y, A_m, A_n):
    print("A: ")
    sp.pprint(A)
    print()
    print("y: ")
    sp.pprint(y)
    print()
    with doc.create(Center()) as center:
        with center.create(Section('Решение уравнения Ax = y')) as sec:
            sec.numbering = None
    doc.append(Math(data=['A = ', pl.Matrix(A)]))
    doc.append(Math(data=['y = ', pl.Matrix(y)]))

    if A_m == A.rank() & A_n == A.rank():
        A_inv = A.inv()
        x = A_inv * y
        print("x = ")
        doc.append(Math(data=['x = ', pl.Matrix(x)]))
        sp.pprint(x)
        doc.generate_pdf('MatrixFile')
        quit()
    else:
        if A_m == A.rank():
            A_pinv = pinverse(A)
        else:
            print("Построим скелетное разложение матрицы А")
            doc.append('Построим скелетное разложение матрицы ')
            doc.append(Math(inline=True, data=['A.'], escape=False))
            B, C = A.rank_decomposition()
            B_size = sp.shape(B)
            C_size = sp.shape(C)
            if B_size[0] == A.rank():
                temp_matrix = C
                C = B
                B = temp_matrix
            print("B = ")
            sp.pprint(B)
            doc.append(Math(data=['B = ', pl.Matrix(B)]))
            print("C = ")
            sp.pprint(C)
            doc.append(Math(data=['C = ', pl.Matrix(C)]))
            C_pinv = pinverse(C)
            B_temp = B.T * B
            B_temp = B_temp.inv()
            print("Найдем псевдообратную матрицу A⁺ по формуле A⁺ = C⁺(B^T B)⁻¹B^T: ")
            doc.append('\nНайдем псевдообратную матрицу ')
            doc.append(Math(inline=True, data=['A^+'], escape=False))
            doc.append('\xa0по формуле: ')
            doc.append(Math(data=['A^+ = C^+(B^T B)^{-1}B^T'], escape=False))
            A_pinv = C_pinv * B_temp * B.T
            sp.pprint(A_pinv)
            doc.append(Math(data=['A^+ = ', pl.Matrix(A_pinv)], escape=False))

    sovmestnost = sovmestnost_check(A, A_pinv, y)
    if sovmestnost:
        print("Система совместна")
        print("Мы можем представить систему в виде x = A⁺y + (E - A⁺A)q")
        doc.append('Система совместна.')
        doc.append('\nМы можем представить систему в виде ')
        doc.append(Math(inline=True, data=['x = A^+y + (E - A^+A)q '], escape=False))
        print("Общее решение системы имеет вид: ")
        doc.append('\nОбщее решение системы имеет вид: ')
        A_pinv_size = sp.shape(A_pinv)
        E = sp.eye(A_pinv_size[0])
        q = sp.Matrix(A_pinv_size[0], 1, lambda i, j: "q_" + str(i + 1))
        x = A_pinv * y + (E - A_pinv * A) * q
        print("x = ")
        sp.pprint(x)
        doc.append(Math(data=['x = ', pl.Matrix(x)]))
    else:
        print("Система не совместна")
        print("Найдем нормальное псевдорешение уравнения: ")
        doc.append('Система не совместна.')
        doc.append('\nНайдем нормальное псевдорешение уравнения: ')
        x = A_pinv * y
        print("x⁰ = A⁺y")
        sp.pprint(x)
        doc.append(Math(data=['x^0 = A^+y = ', pl.Matrix(x)], escape=False))
        print("Длина минимальной невязки равна")
        doc.append('Длина минимальной невязки равна:')
        temp = y - A * x
        temp = temp.T * temp
        nevyazka = temp[0]

        try:
            nevyazka = sp.N(sqrt(nevyazka), 7)
        except Exception:
            nevyazka = sp.sqrt(nevyazka)
        print("∥y-Ax⁰∥ = ")
        sp.pprint(nevyazka)
        doc.append(Math(data=['\|y-Ax^0\| = ', nevyazka], escape=False))
        x_size = sp.shape(x)
        x_length = 0
        for i in range(x_size[0]):
            x_length += x[i] * x[i]
        print("Длинна невязки вектора x⁰ равна")
        print("∥x⁰∥ = ")
        try:
            x_length = sp.N(sqrt(x_length), 7)
        except Exception:
            x_length = sp.sqrt(x_length)
        sp.pprint(x_length)
        doc.append('Длинна невязки вектора ')
        doc.append(Math(inline=True, data=['x^0'], escape=False))
        doc.append('\xa0равна: ')
        doc.append(Math(data=['\|x^0\| = ', x_length], escape=False))
        doc.generate_pdf("Matrix")

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


