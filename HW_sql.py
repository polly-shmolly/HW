import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        password='12345',
        host='127.0.0.1',
        port='5432',
        user='postgres',
        database='test_db'
    )

    cursor = connection.cursor()


# table category
    create_table_category = '''CREATE TABLE category
            (id INT PRIMARY KEY NOT NULL,
            name CHAR[20] NOT NULL,
            description TEXT NOT NULL);
            '''
    cursor.execute(create_table_category)
    connection.commit()


# table discount
    create_table_query = '''CREATE TABLE discount
            (id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            percent INT NOT NULL);
            '''
    cursor.execute(create_table_query)
    connection.commit()

# table product
    create_table_product = '''CREATE TABLE product
    (id INT PRIMARY KEY NOT NULL,
    name CHAR[20] NOT NULL,
    price INT NOT NULL,
    category_id INT,
    discount_id INT,
    
    CONSTRAINT FK_Product_Category FOREIGN KEY (category_id)
    REFERENCES category (id)
    ON DELETE CASCADE,
    
    CONSTRAINT FK_Product_Discount FOREIGN KEY (discount_id)
    REFERENCES discount (id)
    ON DELETE CASCADE
    );
    '''
    cursor.execute(create_table_product)
    connection.commit()

except (Exception, Error) as e:
    print(f'Error when working with PostgreSQL: {e}')
finally:
    if connection:
        connection.close()
        cursor.close()
        print('Connection with PostgreSQL is closed')