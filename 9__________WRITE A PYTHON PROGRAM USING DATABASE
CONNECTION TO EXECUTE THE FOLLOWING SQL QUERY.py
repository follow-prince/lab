import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Create the student table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Insert a new student
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = ("John", 21)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Select all students
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# Delete a student
sql = "DELETE FROM students WHERE name = %s"
val = ("John",)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted.")

# Close the database connection
mydb.close()
