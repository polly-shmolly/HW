# task1
# class SuperStr(str):
#     def is_repeatance(self, s=0):
#         if not isinstance(s, str):
#             return False
#         elif s == 0:
#             return False
#         else:
#             n = len(self) // (len(s))
#             return self == n * s
#
#     def is_palindrom(self, s):
#         return s == s[::-1]
#
#
# s = SuperStr('abcabcabc')
# print(s.is_repeatance('abc')) # t
# print(s.is_repeatance(123123)) # f
# print(s.is_repeatance('abccba')) # f
# print(s.is_repeatance()) # f
# print(s.is_palindrom('abccba')) # t


# task2
# class JsonTask:
#     data = [
#         {
#             "name": "John Smith",
#             "birthday": "02.10.1990",
#             "height": 175,
#             "weight": 76.5,
#             "car": True,
#             "languages": ["C++", "Python"]
#         },
#         {
#             "name": "Alexey Alexeev",
#             "birthday": "05.06.1986",
#             "height": 197,
#             "weight": 101.2,
#             "car": False,
#             "languages": ["Pascal", "Delphi"]
#         },
#         {
#             "name": "Maria Ivanova",
#             "birthday": "28.08.1998",
#             "height": 165,
#             "weight": 56.1,
#             "car": True,
#             "languages": ["C#", "C++", "C"]
#         }
#     ]
#
#     # add new person in data
#     def add_data(self, name, birthday, height, weight, car, languages):
#         new_data = {
#             "name": "",
#             "birthday": "",
#             "height": None,
#             "weight": None,
#             "car": None,
#             "languages": []
#         }
#         new_data['name'] = name
#         new_data['birthday'] = birthday
#         new_data['height'] = height
#         new_data['weight'] = weight
#         new_data['car'] = bool(car)
#         new_data['languages'] = languages
#         JsonTask.data.append(new_data)
#
#     # print data
#     def print_data(self):
#         for i in JsonTask.data:
#             for key, value in i.items():
#                 print(key, value)
#
#     # give information after entering name
#     def name_info(self, name):
#         for i in JsonTask.data:
#             if i['name'] == name:
#                 for key, value in i.items():
#                     print(key, value)
#
#     # language filter
#     def language_filter(self, lang):
#         for i in JsonTask.data:
#             for j in i['languages']:
#                 if j == lang:
#                     print(f'List of employees who use {lang=}: ', i['name'])
#
#     # height filter
#     def height_filter(self, year):
#         amount = 0
#         temp = 0
#         for i in JsonTask.data:
#             year_birth1 = i['birthday']
#             a = year_birth1.split('.')
#             y = int(a[2])
#             if y > year:
#                 temp += i['height']
#                 amount += 1
#         result = temp / amount
#         return result
#
#
# j = JsonTask()
# answer = 0
# while answer != 8:
#     print('\n1 print data\n2 add data\n3 give information after entering name')
#     print('4 language filter\n5 height filter')
#     answer = int(input('\nSelect function to execute: '))
#     if answer == 1:
#         j.print_data()
#     if answer == 2:
#         j.add_data('Jake Slow', '12.03.1990', 202, 80, True, ['Python', 'C++'])
#     if answer == 3:
#         j.name_info('Alexey Alexeev')
#     if answer == 4:
#         j.language_filter('Python')
#     if answer == 5:
#         print(j.height_filter(1900))

