# Necessary imports for working databases
import sqlite3
from sqlite3 import Error

# Use Pandas to make data frames
# If it doesn't work you may need to do "pip install pandas" in terminal
import pandas as pd

# Basic function to connect to the database
def connect_to_database(db_file):
    # Create a database connection to SQLite Database
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        return None
    
    return conn

# Basic function to create a table called "products"
def create_product_table(connection):
    c = connection.cursor()

    try:
        c.execute('''
                CREATE TABLE IF NOT EXISTS products
                ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
                ''')
        
        connection.commit()
        print("Created product table!")
    except Error as e:
        print(e)

# Basic function to insert into the "products" table
def insert_into_product_table(connection):
    c = connection.cursor()

    try:
        c.execute('''
                INSERT INTO products (product_id, product_name)
                    VALUES
                    (1, 'Computer'),
                    (2, 'Printer'),
                    (3, 'Table'),
                    (4, 'Desk'),
                    (5, 'Chair')
                ''')
        
        connection.commit()
        print("Successfuly inserted into products table!")
    except Exception as e:
        print(e)

# Basic function to get all entries in the "products" table
def get_all_products(connection):
    c = connection.cursor()

    try:
        c.execute('''
                  SELECT * FROM products
                  ''')
        df = pd.DataFrame(c.fetchall(), columns = ['Product ID', 'Product Name'])
        print(df)
    except Exception as e:
        print(e)

# Basic function to drop the "products" table
def drop_products_table(connection):
    c = connection.cursor()

    try:
        c.execute('''
                  DROP TABLE IF EXISTS products
                  ''')
        connection.commit()
        print("Successfully dropped products table!")
    except Exception as e:
        print(e)

# Main function
if __name__ == "__main__":
    # Constant for the database
    DATABASE = "back-end/database/banking-software.db"
    
    connection = connect_to_database(DATABASE)
    create_product_table(connection)
    insert_into_product_table(connection)
    get_all_products(connection)
    drop_products_table(connection)

    # Always close your SQLite connection
    connection.close()