# task 1
'''
words substitution
'''

# with open('my_txt/forbidden_words.txt', 'r') as f:
#     for line in f:
#         words = line.lower().split()
#
# with open('my_txt/task1.txt', 'r') as f:
#     text = ''
#     for line in f:
#         text += line
#     for char in text:
#         for i in words:
#             text = text.lower().replace(i, len(i) * '*')
#
# print(text)


"""
запрещеныые слова запихнуть в список
пройтись циклом по этому списку
и в цикле реплейсить i на len(i)*'*'

for i in words:
    text.replace(i,len(i)*'*'
"""


# task2
'''
В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
Вывести на экран всех учащихся, чья оценка меньше 3 баллов
'''

# with open('task2.txt', 'r') as f:
#     for line in f:
#         arr = line.replace('\n', '').split()
#         if int(arr[2]) <= 3:
#             print(line)

# task3
'''
Вычислите сумму всех чисел, записанных в файле.

берет 1х2у3 как одно числоооо 123
'''

# with open('task3.txt', 'r') as f:
#     result = 0
#     for line in f:
#         arr = line.replace('\n', '').split()
#         print(arr)
#         for i in arr:
#             new_arr = ''.join((x for x in i if not x.isalpha()))
#             result += int(new_arr)
#     print(result)

# task4
'''
Cezar cipher
'''

# def caesar_cipher(alphabet, message, step):
#     for letter in message:
#         if letter in alphabet:
#             print(alphabet[(alphabet.index(letter) + step) % len(alphabet)], end='')
#         else:
#             print(letter, end='')
#
#     print()
#
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# with open('task4.txt', 'r') as f:
#     step = 1
#     for line in f:
#         message = line.replace('\n', '').upper()
#         caesar_cipher(alphabet, message, step)
#         step += 1

# task5
'''
В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам.
Каждый избиратель указывает одну партию, за которую он отдает свой голос.
В Государственную Думу попадают партии, которые набрали не менее 7% от числа голосов избирателей.

Дан список партий и список голосов избирателей. Выведите список партий, которые попадут в Государственную Думу.
'''

# with open('task5.txt', 'r') as f:
#     data = f.readlines()
#     data = filter(None, (line.rstrip() for line in data))
#     my_dict = {}
#     summa = 0
#     b = -1
#     for line in data:
#         if line == 'PARTIES:':
#             pass
#         elif line == 'VOTES:':
#             b = 0
#         elif b == -1:
#             my_dict[line] = 0
#         else:
#             summa += 1
#             my_dict[line] += 1
#     for k in my_dict:
#         if 7 * summa / 100 <= my_dict[k]:
#             print(k)
#     print(my_dict)

# task6
'''
Z: Гистограмма

не понимаю как связать словрь с матрицей, 
чтобы сделать эту гистограмму(((
'''

def analysis(lst, dct):
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1

def max_val_dct(dct):
    max_val = 0
    for i in dct.values():
        if max_val < i:
            max_val = i
    return max_val

def zero_matrix(N, M, matrix):
    for i in range(0, M):
        matrix.append([])
        for j in range(0, N):
            matrix[i].append(0)

def gist_matrix(N, M, matrix, dct):

    # for val in dct.values():
    #     for i in range(0, N):
    #         for j in range(0, M):
    #             if val+1 == j:
    #                 matrix[i][j] = 1
    # trans_m = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # for row in trans_m:
    #     print(row)

with open('task6.txt', 'r') as f:
    data = ['']
    my_dict = {}
    for line in f:
        for i in line:
            data += i
    for j in data:
        if j == ' ' or j == '':
            data.remove(' ')
            data.remove('')
    print(data)
    analysis(data, my_dict)
    print(my_dict)
    N = len(data) # horizontal
    M = max_val_dct(my_dict) # vertical
    matrix = []
    zero_matrix(N, M, matrix)
    gist_matrix(N, M, matrix, my_dict)

# task7
'''
Необходимо распределить 450 мест между 
партиями, участвовавших в выборах.
'''
# with open('task7.txt', 'r') as f:
#     summa = 0
#     for line in f:
#         data = line.replace('\n', '').split()
#         summa += int(data[-1])
#     num = summa / 450
#
#     for line in f:
#         data = line.replace('\n', '').split()
#         place = int(data[-1]) / int(num)
#         data[-1] = int(place)
#         print(data)








