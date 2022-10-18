import os

print('OS name:', os.name)
print('Path to dir:', os.getcwd())

# sort files
dirs = ['python_files', 'csv_files', 'text_files']

main_path = 'D:\\TMSnake\\for_hw11'

for i in dirs:
    if not os.path.exists(main_path + '\\' + i):
        os.mkdir(main_path + '\\' + i)

for i in os.listdir(main_path):
    if i.endswith(".py"):
        os.rename(main_path + '\\' + i, f'{main_path}\\python_files\\'+i)
    if i.endswith(".txt"):
        os.rename(main_path + '\\' + i, f'{main_path}\\text_files\\'+i)
    if i.endswith(".csv"):
        os.rename(main_path + '\\' + i, f'{main_path}\\csv_files\\'+i)

# info dir
counter = 0
size = 0
for i in dirs:
    for j in os.listdir(main_path + '\\' + i):
        counter += 1
        size += os.stat(f'{main_path}\\{i}\\{j}').st_size
    print(f'Dir {i} has {counter} files and dir size is {size} bites')
    counter = 0
    size = 0

# python file start
# os.startfile('D:\\TMSnake\\for_hw11\\python_files\\hello_world.py')

# rename file
os.rename(f'{main_path}\\text_files\\task1.txt', f'{main_path}\\text_files\\rename.txt')
print('Файл task1.txt успешно переименован в rename.txt')



