import mysql.connector
from mysql.connector import Error
from sql_password import DB_password

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=DB_password,  # Replace with your MySQL password
            database='railway',  # Ensure this database exists
            port=3307  # Specify the custom port
        )
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None

create_connection()
