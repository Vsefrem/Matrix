from sympy import *

init_printing(use_unicode=True)

def pinverse(matrix):
    """
    Функция для вычисления псевдообратной матрицы.

    Аргументы:
    matrix -- Матрица, экземпляр класса Matrix библиотеки SymPy

    Возвращаемое значение:
    Псевдообратная матрица, экземпляр класса Matrix библиотеки SymPy
    """
    if matrix.shape[0] == matrix.rank():
        matrix_pinv = matrix.T * (matrix * matrix.T).inv()
        return matrix_pinv
    else:
        matrix_b, matrix_c = matrix.rank_decomposition()
        matrix_b_size = shape(matrix_b)
        if matrix_b_size[0] == matrix.rank():
            temp_matrix = matrix_c
            matrix_c = matrix_b
            matrix_b = temp_matrix
        matrix_c_pinv = pinverse(matrix_c)
        matrix_b_temp = matrix_b.T * matrix_b
        matrix_b_temp = matrix_b_temp.inv()
        matrix_pinv = matrix_c_pinv * matrix_b_temp * matrix_b.T
        return matrix_pinv

def orthoprojector_on_core(matrix):
    """
    Функция для вычисления ортопроектора на ядро заданной матрицы по формуле P(N(A)) = I - A^+A.

    Аргументы:
    matrix -- Матрица, экземпляр класса Matrix библиотеки SymPy

    Возвращаемое значение:
    Ортопроектор на ядро, экземпляр класса Matrix библиотеки SymPy
    """
    matrix = pinverse(matrix) * matrix
    matrix = eye(matrix.shape[0]) - matrix
    return matrix

def norm_related_pseudo_sol(matrix_a, column_y, matrix_b, column_z):
    """
    Функция для вычисления нормального связанного псевдорешения по формуле x^*=B^+ z+(AP)^+ (y-AB^+ z),
    а также вывода процесса вычислений на экран.

    Аргументы:
    matrix_a -- Матрица А основного уравнения, экземпляр класса Matrix библиотеки SymPy
    column_y -- Вектор y основного уравнения, экземпляр класса Matrix библиотеки SymPy
    matrix_b -- Матрица B дополнительного уравнения, экземпляр класса Matrix библиотеки SymPy
    column_z -- Вектор z дополнительного уравнения, экземпляр класса Matrix библиотеки SymPy

    Возвращаемое значение:
    Нормальное связанное псевдорешение, экземпляр класса Matrix библиотеки SymPy
    """
    print("Найдем нормальное связанное псевдорешение задачи по формуле x^* = B⁺z+(AP)⁺+(y-AB⁺z)")
    print("A: ")
    pprint(matrix_a)
    print("y: ")
    pprint(column_y)
    print("B: ")
    pprint(matrix_b)
    print("z: ")
    pprint(column_z)
    b_pinv = pinverse(matrix_b)
    print("B⁺: ")
    pprint(b_pinv)
    orp_b = orthoprojector_on_core(matrix_b)
    print("P: ")
    pprint(orp_b)
    ap_pinv = pinverse(matrix_a * orp_b)
    print("(AP)⁺: ")
    pprint(ap_pinv)
    result = b_pinv * column_z + ap_pinv * (column_y - matrix_a * b_pinv * column_z)
    print("Нормальное связанное псевдорешение: ")
    result = expand(result)
    result = simplify(result)
    pprint(Matrix(result))
    return result

def reg_sol(matrix_a, column_y, matrix_b, column_z, r = None, a = None):
    """
    Функция для вычисления регуляризованного решения по формуле x(ra) = (aI + G_op(r)^* * G_op(or))^-1 * G_op(r)^* * g(r),
    а также вывода хода решения.

    Аргументы:
    matrix_a -- Матрица А основного уравнения, экземпляр класса Matrix библиотеки SymPy
    column_y -- Вектор y основного уравнения, экземпляр класса Matrix библиотеки SymPy
    matrix_b -- Матрица B дополнительного уравнения, экземпляр класса Matrix библиотеки SymPy
    column_z -- Вектор z дополнительного уравнения, экземпляр класса Matrix библиотеки SymPy
    r -- значение параметра а, экземпляр класса Symbol библиотеки SymPy
    a -- значение параметра r, экземпляр класса Symbol библиотеки SymPy

    Возвращаемое значение:
    Регуляризованное решение, экземпляр класса Matrix библиотеки SymPy
    """
    if r is None and a is None:
        r, a = symbols('r a')
    elif a is None:
        a = symbols('a')
    elif r is None:
        r = symbols('r')

    print("A: ")
    pprint(matrix_a)
    print("y: ")
    pprint(column_y)
    print("B: ")
    pprint(matrix_b)
    print("z: ")
    pprint(column_z)
    operator_1 = r * matrix_b.T * matrix_b + matrix_a.T * matrix_a
    operator_2 = a * eye(operator_1.shape[0]) + operator_1
    operator_2 = operator_2.inv()
    result = operator_2 * (r * matrix_b.T * column_z + matrix_a.T * column_y)
    print("Регуляризованное решение x(ra) = ")
    result = expand(result)
    result = simplify(result)
    pprint(Matrix(result))
    return result

def parametrization_reg_sol (matrix, r_new = None, a_new = None, e_new = None):
    """
    Функция для параметризации регуляризованного решения.

    Аргументы:
    matrix -- Регуляризованное решение, экземпляр класса Matrix библиотеки SymPy
    r_new -- значение параметра r, экземпляр класса Symbol библиотеки SymPy
    a_new -- значение параметра а, экземпляр класса Symbol библиотеки SymPy
    e_new -- значение параметра e, экземпляр класса Symbol библиотеки SymPy

    Возвращаемое значение:
    Параметризованное регуляризованное решение, экземпляр класса Matrix библиотеки SymPy
    """
    if a_new is not None:
        a = symbols('a')
        matrix = matrix.subs({a: a_new})
    else:
        a_new = symbols('a')
    if r_new is not None:
        r = symbols('r')
        matrix = matrix.subs({r: r_new})
    else:
        r_new = symbols('r')
    if e_new is not None:
        e = symbols('e')
        matrix = matrix.subs({e: e_new})
    else:
        e_new = symbols('e')
    matrix = expand(matrix)
    matrix = simplify(matrix)
    print("Значения параметров:")
    print("a = " + str(a_new))
    print("r = " + str(r_new))
    print("e = " + str(e_new))
    print("Параметризованная матрица: ")
    pprint(Matrix(matrix))
    return matrix







def orthoproektor_na_yadro_sostavnogo_operatora(matrix_a, matrix_b):
    #P(N(Г)) = P(N(B)) * P(N(A * P(N(B))))
    orp_b = orthoprojector_on_core(matrix_b)
    orp_a_b = orthoprojector_on_core(matrix_a * orp_b)
    result = orp_b * orp_a_b
    pprint(result)
    return result

def orthoproektor_na_yadro_sostavnogo_operatora_print(matrix_a, matrix_b):
    #P_(N(Г)) = P(N(B)) * P_(N(A * P(N(B))))
    print("Найдем ортопроектор на ядро составного оператора.")
    print("Матрица A: ")
    pprint(matrix_a)
    print("Матрица B: ")
    pprint(matrix_b)
    orp_b = orthoprojector_on_core(matrix_b)
    print("Ортопроектор P на ядро матрицы B")
    pprint(orp_b)
    orp_a_b = orthoprojector_on_core(matrix_a * orp_b)
    print("Ортопроектор на ядро матрицы AP: ")
    pprint(orp_a_b)
    result = orp_b * orp_a_b
    print("Ортопроектор на ядро составного оператора: ")
    pprint(result)
    return result

def lim_param_resh (matrix):
    n = symbols('n')
    expr = limit(matrix, n, 00)
    pprint(expr)
    return expr

def orthoproektor_na_obraz(matrix):
    #P(R(A)) = AA^+
    matrix = matrix * pinverse(matrix)
    return matrix

def pinverse_print(matrix):
    if matrix.shape[0] == matrix.rank():
        print("Строки матрицы C л.н. => матрица CC^T обратима.")
        print("Найдем псевдообратную матрицу по формуле C⁺ = C^T (CC^T)⁻¹:")
        matrix = matrix.T * (matrix * matrix.T).inv()
        print("C⁺: ")
        Matrix(matrix)
        return matrix
    else:
        print("Построим скелетное разложение матрицы А")
        matrix_b, matrix_c = matrix.rank_decomposition()
        matrix_b_size = shape(matrix_b)
        if matrix_b_size[0] == matrix.rank():
            temp_matrix = matrix_c
            matrix_c = matrix_b
            matrix_b = temp_matrix
        print("B = ")
        Matrix(matrix_b)
        print("C = ")
        Matrix(matrix_c)
        matrix_c_pinv = pinverse_print(matrix_c)
        matrix_b_temp = matrix_b.T * matrix_b
        matrix_b_temp = matrix_b_temp.inv()
        print("Найдем псевдообратную матрицу A⁺ по формуле A⁺ = C⁺(B^T B)⁻¹B^T: ")
        matrix_pinv = matrix_c_pinv * matrix_b_temp * matrix_b.T
        Matrix(matrix_pinv)
        return matrix_pinv

# def obshee_svyazanoe_with_print(matrix_a, column_y, matrix_b, column_z):
#     #x = x^* + Qu
#     norm_resh = norm_svyazanoe_pseudoresh_with_print(matrix_a, column_y, matrix_b, column_z)
#     Q = orthoproektor_na_yadro_sostavnogo_operatora(matrix_a, matrix_b)
#     x = norm_resh + Q *