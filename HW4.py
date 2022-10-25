# -----Part1-----
# task1 FORMULAS

# import math
#
# def formula1():
#     summa = 0
#     next_part = 1
#     x = 0.6
#     while x <= 1.1:
#         for n in range(10, 16):
#             for k in range(1, n + 1):
#                 next_part = pow(math.log(abs(x + k)), 2) * math.cos((k + math.pow(math.sin(x), 1 / 5)) / k * x)
#                 summa += next_part
#             res = 1 / 45 * pow(pow(3, x + n), 1 / 2) * summa
#             print('x:', x, 'n:', n, 'res:%.2f' % res)
#             summa = 0
#         x += 0.25
#
# def formula2():
#     summa = 0
#     next_part = 1
#     x = 0.6
#     e = 2.718
#     pi = 3.14
#     while x <= 1.1:
#         for n in range(10, 16):
#             for k in range(1, n + 1):
#                 next_part = pow(pow(pow(x, k + 1), 1/k) + pow(pow(e, x - 3), 1/k), 1/2) / (1 + math.log(x, 10))
#                 summa += next_part
#             res = math.sin(math.radians(pi * n / (x + 3))) * summa
#             print('x:', x, 'n:', n, 'res:%.2f' % res)
#             summa = 0
#         x += 0.25
#
# def formula3():
#     summa = 0
#     next_part = 1
#     x = 0.6
#     e = 2.718
#     while x <= 1.1:
#         for n in range(10, 16):
#             for k in range(1, n + 1):
#                 next_part = (1 + (k + 1) / n) / pow(e, k) * pow(x, k - 1) + math.log(x, 10)
#                 summa += next_part
#             res = pow(pow(math.sin(math.radians(x/n)), 3), 1/2) * summa
#             print('x:', x, 'n:', n, 'res:%.2f' % res)
#             summa = 0
#         x += 0.25
#
#
# def formula4():
#     summa = 0
#     next_part = 1
#     x = 0.6
#     e = 2.718
#     pi = 3.14
#     while x <= 1.1:
#         for n in range(10, 16):
#             for k in range(1, n + 1):
#                 next_part = pow(math.sin((k - 1)/(k + 1)), 2) + pow(e, pow(x/k, 1/2))
#                 summa += next_part
#             res = pi / pow(x, 3) + (3 / (x + 5)) * summa
#             print('x:', x, 'n:', n, 'res:%.2f' % res)
#             summa = 0
#         x += 0.25
#
# my_answer = int(input('Enter formula from HW (1-4): '))
#
# if my_answer == 1:
#     formula1()
# elif my_answer == 2:
#     formula2()
# elif my_answer == 3:
#     formula3()
# elif my_answer == 4:
#     print('%.2f'% formula4())
# else:
#     print('There was no such formula!')


# -----Part2-----

# task1
'''
Program finds elements 
divisible by 15
'''
# import random
# elements = int(input('Enter elements amount: '))
# arr = [random.randint(1, 100) for x in range(elements)]
# print(arr)
# print(list(filter(lambda x: x % 15 == 0, arr)))

# task2
'''
program find unique numbers
from array 
'''
# import random
# def unique(arr):
#     arr2 = [n for n in arr if arr.count(n) == 1]
#     S = set(arr2)
#     print(' '.join(str(arr) for arr in S))
#
# arr = [random.randint(1, 50) for x in range(15)]
# n = len(arr) - 1
# print(arr)
# unique(arr)

# task3 CEZAR CIPHER
# Eng
# def encrpt(text):
#     '''
#     :param text: text you want cipher
#     :return: cipher text
#     '''
#     encryption = ''
#     for i in text:
#         if i.isupper():
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('A')
#             new_index = (i_index + 3) % 26
#             new_unicode = new_index + ord('A')
#             new_char = chr(new_unicode)
#             encryption = encryption + new_char
#         else:
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('a')
#             new_index = (i_index + 3) % 26
#             new_unicode = new_index + ord('a')
#             new_char = chr(new_unicode)
#             encryption = encryption + new_char
#     return encryption
#
# def decrpt(text):
#     '''
#     :param text: ciphered text
#     :return: normal text
#     '''
#     good_text = ''
#     for i in text:
#         if i.isupper():
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('A')
#             new_index = (i_index - 3) % 26
#             new_unicode = new_index + ord('A')
#             new_char = chr(new_unicode)
#             good_text = good_text + new_char
#         else:
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('a')
#             new_index = (i_index - 3) % 26
#             new_unicode = new_index + ord('a')
#             new_char = chr(new_unicode)
#             good_text = good_text + new_char
#     return good_text
#
# my_text = input('Enter your text message: ')
# print('Encrypted text: ', encrpt(my_text))
#
# print('Decrypted text: ', decrpt(encrpt(my_text)))

# Rus
# def encrpt(text):
#     '''
#     :param text: text you want cipher
#     :return: cipher text
#     '''
#     encryption = ''
#     for i in text:
#         if i.isupper():
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('А')
#             new_index = (i_index + 3) % 32
#             new_unicode = new_index + ord('А')
#             new_char = chr(new_unicode)
#             encryption = encryption + new_char
#         else:
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('а')
#             new_index = (i_index + 3) % 32
#             new_unicode = new_index + ord('а')
#             new_char = chr(new_unicode)
#             encryption = encryption + new_char
#     return encryption
#
# def decrpt(text):
#     '''
#     :param text: ciphered text
#     :return: normal text
#     '''
#     good_text = ''
#     for i in text:
#         if i.isupper():
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('А')
#             new_index = (i_index - 3) % 32
#             new_unicode = new_index + ord('А')
#             new_char = chr(new_unicode)
#             good_text = good_text + new_char
#         else:
#             i_unicode = ord(i)
#             i_index = ord(i) - ord('а')
#             new_index = (i_index - 3) % 32
#             new_unicode = new_index + ord('а')
#             new_char = chr(new_unicode)
#             good_text = good_text + new_char
#     return good_text
#
# my_text = input('Введите сообщения для шифрования: ')
# print('Зашифрованнный тект: ', encrpt(my_text))
#
# print('Расшифрованный текст: ', decrpt(encrpt(my_text)))

# En
# def encrpt(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     res = ''
#     for i in text:
#         i_index = alphabet.find(i)
#         new_index = i_index + 3
#         if i in alphabet:
#             res += alphabet[new_index]
#     return res
#
# my_text = input('Enter your message: ')
# print(encrpt(my_text))

