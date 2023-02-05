import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='5356394RA',
    database='my_first_db'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")
mycursor.execute("ALTER TABLE student MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ("01", "John")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = ("01", "John", 10000)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


