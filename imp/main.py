import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="test")

if connection.is_connected():
	print('Connected!')
else:
	print('Fail')

connection.close()

import mysql.connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        return connection
    except mysql.connector.Error as err:
        print("Error: Unable to connect to the database")
        print(err)
        return None

def create_table(connection):
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS dummy_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        column1 VARCHAR(255),
        column2 VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

# Add data to the database
def add_data(connection, data):
    cursor = connection.cursor()
    query = "INSERT INTO dummy_table (column1, column2) VALUES (%s, %s)"
    cursor.execute(query, data)
    connection.commit()
    cursor.close()

# Delete data from the database
def delete_data(connection, record_id):
    cursor = connection.cursor()
    query = "DELETE FROM dummy_table WHERE id = %s"
    cursor.execute(query, (record_id,))
    connection.commit()
    cursor.close()

# Edit data in the database
def edit_data(connection, record_id, new_data):
    cursor = connection.cursor()
    query = "UPDATE dummy_table SET column1 = %s, column2 = %s WHERE id = %s"
    cursor.execute(query, (new_data[0], new_data[1], record_id))
    connection.commit()
    cursor.close()

# Show data from the database
def show_data(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM dummy_table"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

if __name__ == "__main__":
    connection = connect_to_database()
    
    if connection:
        # Perform operations
        create_table(connection)
        data_to_add = ("value1", "value2")
        add_data(connection, data_to_add)

        record_id_to_delete = 1
        delete_data(connection, record_id_to_delete)

        record_id_to_edit = 2
        new_data = ("new_value1", "new_value2")
        edit_data(connection, record_id_to_edit, new_data)

        data = show_data(connection)
        for row in data:
            print(row)
        
        connection.close()
