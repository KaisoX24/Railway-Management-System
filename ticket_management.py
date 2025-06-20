from database_config import create_connection

def book_ticket(name, phone, age, gender, start, destination, travel_date):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = """INSERT INTO railway (name, phno, age, gender, from_f, to_t, date_d)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""" 
            cursor.execute(query, (name, phone, age, gender, start, destination, travel_date))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()

def check_ticket(phone):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM railway WHERE phno = %s"
            cursor.execute(query, (phone,))
            ticket = cursor.fetchone()
            return ticket
        except:
            return None
        finally:
            cursor.close()
            conn.close()

def cancel_ticket(phone):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = "DELETE FROM railway WHERE phno = %s"
            cursor.execute(query, (phone,))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()
