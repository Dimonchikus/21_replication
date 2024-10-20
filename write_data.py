import mysql.connector
import time

def insert_data():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpass",
        database="mydb",
        port=3306
    )
    cursor = connection.cursor()

    while True:
        cursor.execute("INSERT INTO test_table (name) VALUES ('test_data')")
        connection.commit()
        time.sleep(2)

if __name__ == "__main__":
    insert_data()
