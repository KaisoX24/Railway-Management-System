# user_management.py
from database_config import create_connection
from mysql.connector import Error

def register_user(username, password, first_name, last_name, phone, gender, dob, age):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = """INSERT INTO user_accounts (user_name, password, fname, lname, phno, gender, dob, age)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (username, password, first_name, last_name, phone, gender, dob, age))
            conn.commit()
            return True
        except Error as e:
            print("Error in register_user:", e)
            return False
        finally:
            cursor.close()
            conn.close()

def verify_login(username, password):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT password FROM user_accounts WHERE user_name = %s", (username,))
            result = cursor.fetchone()
            
            if result is None:
                return 0  # Username does not exist
            elif result[0] != password:
                return 1  # Incorrect password
            else:
                return 2  # Successful login
        except Error as e:
            print("Error in verify_login:", e)
            return -1  # Indicates an error occurred
        finally:
            cursor.close()
            conn.close()
