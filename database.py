from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_mysql_username'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'feedback_db'

mysql = MySQL(app)

def create_table():
    with app.app_context():  # Use the application context
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()

def insert_feedback(name, email, message):
    with app.app_context():  # Use the application context
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO feedback (name, email, message)
            VALUES (%s, %s, %s)
        ''', (name, email, message))
        conn.commit()
        cursor.close()

def fetch_feedback():
    with app.app_context():  # Use the application context
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM feedback')
        feedbacks = cursor.fetchall()
        cursor.close()
        return feedbacks
