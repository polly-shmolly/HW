# task1
'''
Классы Товар и Склад
'''
#
from dataclasses import dataclass
#
#@dataclass
# class Product:
#     name: str
#     name_store: str
#     cost: int
#
#
# class Storage(Product):
#
#     def __init__(self):
#         self.list_of_products = []
#
#     def add_to_list(self, product):
#         return self.list_of_products.append(product)
#
#
#     def search_id(self, index):
#         for i in range(len(self.list_of_products)):
#             if index == i:
#                 return self.list_of_products[i]
#
#     def search_name(self):
#         name = input('Enter name of product: ')
#         for i in self.list_of_products:
#             if i.name == name:
#                 return i
#
#     def sort_name_store(self):
#         return sorted(self.list_of_products, key=lambda product: product.name_store)
#
#     def sort_cost(self):
#         return sorted(self.list_of_products, key=lambda product: product.cost)
#
#     def sort_name(self):
#         return sorted(self.list_of_products, key=lambda product: product.name)
#
#     # не вызываю потому что бьет ошибку и я не знаю почему(((
#     # может и имею представление, потому что у меня нет инита в этом кдассе, но я не понимю....
#     def __add__(self, other):
#         return self.cost + other.cost
#
#
# a = Product('Book', 'Oz.by', 12)
# b = Product('Bottle', 'Aliexpress', 6)
# c = Product('Sweet', 'Milka', 14)
# storage = Storage()
# storage.add_to_list(a)
# storage.add_to_list(b)
# storage.add_to_list(c)
#
# print(storage.search_id(2))
# print('-------------------------------')
# print("!!!")
# print(storage.search_name())# я вообще имею право так делать????
# print('-------------------------------')
# print(storage.sort_name_store())
# print('-------------------------------')
# print(storage.sort_name())
# print('-------------------------------')
# print(storage.sort_cost())

# task2
'''
Класс Разговор
'''
# class Talking:
#     counter = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def to_answer(self):
#         yes = 'moore-moore'
#         no = 'meow-meow'
#         if self.counter % 2 == 0:
#             self.counter += 1
#             return yes
#         else:
#             self.counter += 1
#             return no
#
#     def number_yes(self):
#         counter_yes = 0
#         counter = self.counter
#
#         while counter > 0:
#             if counter % 2 == 1:
#                 counter_yes += 1
#             counter -= 1
#
#         return counter_yes
#
#     def number_no(self):
#         counter_no = 0
#         counter = self.counter
#         while counter > 0:
#             if counter % 2 == 0:
#                 counter_no += 1
#             counter -= 1
#         return counter_no
#
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')


# task3
'''
Класс Темы
'''
# class Themes:
#     def __init__(self, lst: list):
#         self.lst = lst
#
#     def add_theme(self, value):
#         return self.lst.append(value)
#
#     def shift_one(self):
#         return self.lst.insert(0, self.lst.pop())
#
#     def reverse_order(self):
#         return self.lst.reverse()
#
#     @property
#     def get_themes(self):
#         return self.lst
#
#     @property
#     def get_first(self):
#         return self.lst[0]
#
# t1 = Themes(['weather', 'rain'])
# t1.add_theme('warm')
# print(t1.get_themes)
# t1.shift_one()
# print(t1.get_themes)
# t1.reverse_order()
# print(t1.get_themes)
# print(t1.get_first)


# task4
'''
Класс "ПчелоСлон"
'''
# class BeeElephant:
#     def __init__(self, bee, elephant):
#         self.bee = bee
#         self.elephant = elephant
#
#     def fly(self):
#         if self.bee > self.elephant:
#             return True
#         return False
#
#     def trumplet(self):
#         if self.elephant > self.bee:
#             return 'tu-tu-doo-doo'
#         return 'wzzzz'
#
#     def eat(self, meal, value):
#         if meal == 'nectar':
#             self.bee += value
#             if self.bee > 100: # явно есть проще вариант, но мне пришло только это в голову
#                 self.bee = 100
#             self.elephant -= value
#             if self.elephant < 0:
#                 self.elephant = 0
#         if meal == 'grass':
#             self.elephant += value
#             if self.elephant > 100:
#                 self.elephant = 100
#             self.bee -= value
#             if self.bee < 0:
#                 self.bee = 0
#
#     def get_parts(self):
#         return [self.bee, self.elephant]
#
# be = BeeElephant(3, 2)
# print(be.fly())
# print(be.trumplet())
# be.eat('grass', 4)
# print(be.get_parts())


# task5
'''
Класс Прямоугольный треугольник
'''
# import math
# class RectangularTriangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def size_side_a(self, percentage):
#         if percentage < 0:
#             self.a = self.a - (self.a * abs(percentage) / 100)
#         self.a = (self.a * percentage / 100) + self.a
#         return self.a
#
#     def r_circle(self):
#         return 1/2 * (self.a**2 + self.b**2) ** (0.5)
#
#     def p_triangle(self):
#         return self.a + self.b + (self.a**2 + self.b**2) ** (0.5)
#
#     def angle_3(self):
#         alfa = math.asin(self.a / (self.a**2 + self.b**2) ** (0.5))
#         print(f'alfa = {math.degrees(alfa)}')
#         beta = 90 - math.degrees(alfa)
#         print(f'beta = {beta}')
#         print('gama = 90')
#
# t = RectangularTriangle(4, 5)
# print(t.size_side_a(40))
# print(f'radius = {t.r_circle()}')
# print(f'perimeter = {t.p_triangle()}')
# t.angle_3()

# task6
'''
Класс Одномерный массив
'''
# class TArray:
#     def __init__(self, amount):
#         self.amount = amount
#         self.arr = []
#     def add_data(self):
#
#         for i in range(self.amount):
#             num = int(input('Enter element: '))
#             self.arr.append(num)
#     def print_data(self):
#         print(self.arr)
#     def max_min(self):
#         max_el = self.arr[0]
#         min_el = self.arr[0]
#         for i in range(self.amount):
#             if max_el < self.arr[i]:
#                 max_el = self.arr[i]
#             if min_el > self.arr[i]:
#                 min_el = self.arr[i]
#         print(f'{max_el=}, {min_el=}')
#     def sort_list(self):
#         self.arr.sort()
#         return self.arr
#     def sum_elem(self):
#         counter = 0
#         for i in range(self.amount):
#             counter += self.arr[i]
#         return counter
#     def __add__(self, other):
#         return self.arr.append(other)
#     def __mul__(self, other):
#         for i in range(self.amount):
#             self.arr[i] *= other
#
#
# a = TArray(5)
# a.add_data()
# a.print_data()
# a.max_min()
# print(a.sort_list())
# print(a.sum_elem())
# a+5
# a.print_data()
# a*2
# a.print_data()




