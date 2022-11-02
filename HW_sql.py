import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(
        password='12345',
        host='127.0.0.1',
        port='5432',
        user='postgres',
        database='test_db'
    )

# create tables
# try:
#     cursor = connection.cursor()
#
# # table category
#     create_table_category = '''CREATE TABLE category
#             (id INT PRIMARY KEY NOT NULL,
#             name TEXT NOT NULL,
#             description TEXT NOT NULL);
#             '''
#     cursor.execute(create_table_category)
#     connection.commit()
#
# # table discount
#     create_table_query = '''CREATE TABLE discount
#             (id INT PRIMARY KEY NOT NULL,
#             name TEXT NOT NULL,
#             percent INT NOT NULL);
#             '''
#     cursor.execute(create_table_query)
#     connection.commit()
#
# # table product
#     create_table_product = '''CREATE TABLE product
#     (id INT PRIMARY KEY NOT NULL,
#     name TEXT NOT NULL,
#     price INT NOT NULL,
#     category_id INT,
#     discount_id INT,
#
#     CONSTRAINT FK_Product_Category FOREIGN KEY (category_id)
#     REFERENCES category (id)
#     ON DELETE CASCADE,
#
#     CONSTRAINT FK_Product_Discount FOREIGN KEY (discount_id)
#     REFERENCES discount (id)
#     ON DELETE CASCADE
#     );
#     '''
#     cursor.execute(create_table_product)
#     connection.commit()
#
# except (Exception, Error) as e:
#     print(f'Error when working with PostgreSQL: {e}')
# finally:
#     if connection:
#         connection.close()
#         cursor.close()
#         print('Connection with PostgreSQL is closed')

# insert values in tables
# with connection.cursor() as cursor:
#  # category
#     insert_category = '''
#     INSERT INTO category (id, name, description) VALUES (1, 'one', 'hello')
#     '''
#     cursor.execute(insert_category)
#     connection.commit()
#
#     insert_category = '''
#         INSERT INTO category (id, name, description) VALUES (2, 'two', 'hello hello')
#         '''
#     cursor.execute(insert_category)
#     connection.commit()
#
#     insert_category = '''
#         INSERT INTO category (id, name, description) VALUES (3, 'three', 'hello hello hello')
#         '''
#     cursor.execute(insert_category)
#     connection.commit()
#
# # discount
#     insert_discount = '''
#         INSERT INTO discount (id, name, percent) VALUES (1, 'discount1', 10)
#         '''
#     cursor.execute(insert_discount)
#     connection.commit()
#
#     insert_discount = '''
#              INSERT INTO discount (id, name, percent) VALUES (2, 'discount2', 20)
#              '''
#     cursor.execute(insert_discount)
#     connection.commit()
#
#     insert_discount = '''
#                   INSERT INTO discount (id, name, percent) VALUES (3, 'discount3', 30)
#                   '''
#     cursor.execute(insert_discount)
#     connection.commit()
#
#  # product
#     insert_product = '''
#              INSERT INTO product (id, name, price, category_id, discount_id) VALUES (1, 'product1', 250, 2, 3)
#              '''
#     cursor.execute(insert_product)
#     connection.commit()
#
#     insert_product = '''
#              INSERT INTO product (id, name, price, category_id, discount_id) VALUES (2, 'product2', 140, 1, 2)
#              '''
#     cursor.execute(insert_product)
#     connection.commit()
#
#     insert_product = '''
#             INSERT INTO product (id, name, price, category_id, discount_id) VALUES (3, 'product3', 400, 3, 1)
#             '''
#     cursor.execute(insert_product)
#     connection.commit()

# simple query
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_products = "SELECT name, discount_id from product"
products = execute_read_query(connection, select_products)
for product in products:
    print(product)

print('---')
select_products_discount = '''
SELECT product.id, product.name, discount.percent
FROM discount
INNER JOIN product ON discount.id = product.discount_id
'''
products_discounts = execute_read_query(connection, select_products_discount)
for product_discount in products_discounts:
    print(product_discount)

# print('--- тут ошибка хз че такое')
# select_discount_category_product = '''
# SELECT product.name, discount.percent,
# description as category
# FROM discount
# INNER JOIN discount ON discount.id = product.discount_id
# INNER JOIN product ON category.id = product.category_id
# '''
# discount_category_product = execute_read_query(
#     connection, select_discount_category_product
# )
# for i in discount_category_product:
#     print(i)
