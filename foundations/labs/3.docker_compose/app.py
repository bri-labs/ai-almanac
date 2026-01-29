from flask import Flask
import mysql.connector
import time

app=Flask(__name__)

DB_CONFIG={
    "host": "db",
    "user": "user",
    "password": "password",
    "database": "testdb"
}

# Connect to database
def get_db_connection():
    # along with retry logic if any error happens
    for i in range(10):
        try:
            conn=mysql.connector.connect(**DB_CONFIG)
            return conn
        except:
            print("Waiting for database")
            time.sleep(3)

    raise Exception("Database connection failed")

# Homepage route
@app.route("/")
def read_data():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("Select * from messages")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()

    return {
        "messages": rows
    }

# Add data
@app.route("/add")
def add_data():
    conn=get_db_connection()
    cursor=conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        text VARCHAR(255)
        )
    """)

    cursor.execute("""
        INSERT INTO messages (text) VALUES ('Hello from Docker + MySQL!')
                   """)
    
    conn.commit()
    cursor.close()
    conn.close()

    return "Message inserted into the database"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)