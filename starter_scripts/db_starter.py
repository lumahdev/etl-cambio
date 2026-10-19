import mysql.connector
from mysql.connector import Error
from db_functions import execute_query


def create_server_connection(db_name=None):
    connection = None

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Senha@123',
            database=db_name
        )
        print("MySQL Database connection successful")

    except Error as err:
        print(f"Error: '{err}'")

    return connection


first_connection = create_server_connection()

execute_query(first_connection, "CREATE DATABASE IF NOT EXISTS cambios;")

connection = create_server_connection("cambios")

execute_query(connection, """
CREATE TABLE IF NOT EXISTS currencies (
    currency_id INT PRIMARY KEY AUTO_INCREMENT,
    iso_code VARCHAR(3) NOT NULL,
    iso_numeric VARCHAR(3) NOT NULL,
    name VARCHAR(100) NOT NULL,
    symbol VARCHAR(5) NOT NULL
);""")

execute_query(connection, """
CREATE TABLE IF NOT EXISTS rates (
    rate_id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    quote INT NOT NULL,
    rate DECIMAL(20,10) NOT NULL,

    FOREIGN KEY (quote) REFERENCES currencies(currency_id),
    UNIQUE (quote, date),
    INDEX idx_date (date)
);""")