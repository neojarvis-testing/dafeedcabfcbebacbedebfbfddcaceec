import mysql.connector
print("mysql connector is installed")
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password='examly'
)
cur = connection.cursor()