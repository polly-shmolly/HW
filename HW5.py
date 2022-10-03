# -----Part1 MATRIX------
# task1
'''
Выполнить обработку элементов
прямоугольной матрицы А,
имеющей N строк и М столбцов.
Найти сумму элементов всей матрицы.
Определить, какую долю в этой сумме
составляет сумма элементов каждого столбца.
Результат оформить в виде матрицы
из N+1 строк и M столбцов.
'''
import random

def rand_matrx(matrix, N, M):
    for i in range(0, N):
        matrix.append([])
        for j in range(0, M):
            matrix[i].append(random.randint(0, 50))
        print(matrix[i])

def print_matrix(matrix, N, M):
    for row in matrix:
        print(row)

# def sum_matrix(matrix, N, M):
#     '''
#     :param matrix: matrix
#     :param N: row
#     :param M: column
#     :return: sum of all elements in matrix
#     '''
#     summa = 0
#     for i in range(0, N):
#         for j in range(0, M):
#            summa += matrix[i][j]
#     return summa
#
# def column_perc(matrix, N, M, summa):
#     '''
#     :param matrix: matrix
#     :param N: row
#     :param M: column
#     :param summa: sum of all elements in matrix
#     :return: none
#     '''
#     new_elem = 0 # percentage in a column
#     summa_column = 0
#     for i in range(0, N):
#         for j in range(0, M):
#             summa_column += matrix[i][j]
#         new_elem = int(summa_column / summa * 100)
#         matrix[i].append(new_elem)
#         summa_column = 0
#
# A = []
# N = 4
# M = 5
# rand_matrx(A, N, M)
# print('---')
# summa = sum_matrix(A, N, M)
# print('Sum: ', summa)
# print('---')
# column_perc(A, N, M, summa)
# print_matrix(A, N + 1, M)

# task2
'''
Выполнить обработку элементов прямоугольной матрицы А, 
имеющей N строк и М столбцов. 
Перемножить элементы каждого столбца матрицы 
с соответствующими элементами Кго столбца.
'''

# def proizv_elem(matrix, N, M, k):
#     '''
#     :param matrix: matrix
#     :param N: row
#     :param M: column
#     :param k: user column
#     :return: new matrix
#     '''
#     for i in range(0, N):
#         for j in range(0, M):
#             matrix[i][j] = matrix[i][j] * matrix[i][k]
#     return matrix
#
# A = []
# N = 4
# M = 5
# rand_matrx(A, N, M)
# print('---')
# proizv_elem(A, N, M, 2)
# print_matrix(A, N, M)


# task3
'''
Выполнить обработку элементов прямоугольной матрицы А, 
имеющей N строк и М столбцов. 
Просуммировать элементы каждой строки матрицы 
с соответствующими элементами Lтой строки.
'''

# def proizv_elem(matrix, N, M, l):
#     '''
#     :param matrix: matrix
#     :param N: row
#     :param M: column
#     :param l: user column
#     :return: new matrix
#     '''
#     for i in range(0, N):
#         for j in range(0, M):
#             matrix[i][j] = matrix[i][j] + matrix[l][j]
#     return matrix
#
# A = []
# N = 4
# M = 5
# rand_matrx(A, N, M)
# print('---')
# proizv_elem(A, N, M, 2)
# print_matrix(A, N, M)

# task4
'''
Выполнить обработку элементов прямоугольной матрицы А, 
имеющей N строк и М столбцов. 
Все элементы имеют целый тип. 
Дано целое число Н. Определить, какие столбцы 
имеют хотя бы одно такое число, а какие не имеют.

думаю, что сделалал не так как нужно
'''
# def is_num(matrix,N, M, H):
#     for i in range(0, N):
#         for j in range(0, M):
#             if matrix[i][j] == H:
#                 print('H is in column', j)
#
# A = []
# N = 4
# M = 5
# rand_matrx(A, N, M)
# print(is_num(A, N, M, 5))



# task5
'''
Выполнить обработку элементов квадратной матрицы А, 
имеющей N строк и N столбцов. Найти сумму элементов, 
стоящих на главной диагонали, 
и сумму элементов, стоящих на побочной диагонали
'''
# def diagonal1(matrix, N):
#     summa = 0
#     for i in range(0, N):
#         for j in range(0, N):
#             if i == j:
#                 summa += matrix[i][j]
#     return summa
#
# def diagonal2(matrix, N):
#     summa = 0
#     for i in range(0, N):
#         for j in range(0, N):
#             if i + j == N - 1:
#                 summa += matrix[i][j]
#     return summa
#
# A = []
# N = 4
# rand_matrx(A, N, N)
# print('Main diagonal sum: ', diagonal1(A, N))
# print('Underplot diagonal sum: ', diagonal2(A, N))


# task6
'''
matrix in spiral
'''



# -----Part 2------
# task1
'''
checking a number for
primality using recursion
'''

# def rec_prim(num, divider = None):
#     '''
#     :param num: number to checking
#     :param divider: divider
#     :return: is the number primality
#     '''
#     if num == 1:
#         return False
#     elif divider is None:
#         divider = num - 1
#     while divider > 1:
#         if num % divider == 0:
#             return False
#         else:
#             return rec_prim(num, divider - 1)
#     else:
#         return True
#
# print('Is primality: ', rec_prim(10))


# task2
'''
finding the greatest
common divisor using recursion
'''

# def rec_gcd(num1, num2):
#     '''
#     :param num1: first number
#     :param num2: second number
#     :return: the greatest common divisor
#     '''
#     if (num1 == 0):
#         return num2
#     elif (num2 == 0):
#         return num1
#     else:
#         return rec_gcd(num2, num1 % num2)
#
# print('The greatest common divisor is: ', rec_gcd(64, 24))


# task3
'''
Vigenere cipher: 
Encryption and decryption 
of a message
'''

# def encrypt(message, key):
#     new_unicode = 0
#     new_chr = ''
#     encrypt_mes = ''
#     id_key = 0
#     for i in message:
#         new_unicode = ((ord(i) - ord('A')) + (ord(key[id_key]) - ord('A'))) % 26
#         new_chr = chr(new_unicode + ord('A'))
#         encrypt_mes += new_chr
#         id_key += 1
#         if id_key >= len(key):
#             id_key = 0
#     return encrypt_mes
#
#
# def decrypt(message, key):
#     new_unicode = 0
#     new_chr = ''
#     encrypt_mes = ''
#     id_key = 0
#     for i in message:
#         new_unicode = ((ord(i) - ord('A')) - (ord(key[id_key]) - ord('A')) + 26) % 26
#         new_chr = chr(new_unicode + ord('A'))
#         encrypt_mes += new_chr
#         id_key += 1
#         if id_key >= len(key):
#             id_key = 0
#     return encrypt_mes
#
# print(encrypt('ABCD', 'KEY'))
# print(decrypt(encrypt('ABCD', 'KEY'), 'KEY'))


# task4
'''
rotating lattice method
'''

# task5
'''
binary search
'''
# def binary_search(arr, num, start, end):
#     mid = (start + end) // 2
#     if num == arr[mid]:
#         return mid
#     elif num < arr[mid]:
#         return binary_search(arr, num, start, mid - 1)
#     else:
#         return binary_search(arr, num, mid + 1, end)
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# start = 0
# end = len(arr)
# num = 6
# print('Searching for:', num, '\nIndex:', binary_search(arr, num, start, end))

