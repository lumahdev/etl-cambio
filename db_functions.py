from mysql.connector import Error

def execute_many_query(connection, query, params=None):
    cursor = connection.cursor()

    try:
        cursor.executemany(query, params)

    except Error as err:
        connection.rollback()
        print(f"Error: '{err}'")

    finally:
        cursor.close()


def return_execute_query(connection, query, params=None):
    cursor = connection.cursor()

    try:
        cursor.execute(query, params)

    except Error as err:
        connection.rollback()
        print(f"Error: '{err}'")

    finally:
        return cursor


def execute_query(connection, query, params=None):
    cursor = connection.cursor()

    try:
        cursor.execute(query, params)
        connection.commit()

    except Error as err:
        connection.rollback()
        print(f"Error: '{err}'")

    finally:
        cursor.close()