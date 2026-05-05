import mysql.connector

def connect():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="movies_db"
        )
        return conn
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL database: ", error)

def execute_query(query, data=None):
    """Executes a query on the MySQL database."""
    conn = connect()
    cursor = conn.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as error:
        print("Error while executing query: ", error)
    finally:
        cursor.close()
        conn.close()
