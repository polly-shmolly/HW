# есть список например [2, 7, 11, 15] и target=9.
# Найти в списке  элементы которые в сумме дают таргет.
# Например тут это 0-й и 1-й элементы, 2+7=9.
# Учитывать, что элементы могут не идти друг за другом.

# my_list = [2, 10, 7, 15, 4, 5]
# target = 9
#
# my_list = sorted(my_list)
#
# first = 0
# last = len(my_list) - 1
#
# while first < last:
#     s = my_list[first] + my_list[last]
#     if s == target:
#         print(f'index: {first}, {last}\nelements: {my_list[first]}, {my_list[last]}')
#         first += 1
#         last -= 1
#     if s < target:
#         first += 1
#     if s > target:
#         last -= 1



# модификация задачи: на входе не список, а диапазон например от -10 до 10.
# Так же есть таргет, найти элементы из диапазона которые в сумме дают таргет

target = 5

first = -10
last = 10

while first < last:
    s = first + last
    if s == target:
        print(f'elements: {first}, {last}')
        first += 1
        last -= 1
    if s < target:
        first += 1
    if s > target:
        last -= 1
