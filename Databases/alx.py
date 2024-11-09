import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'WJ28@krhps',
    database = 'dom'
)

mycursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
);
""")

print("Table created successfully!")

# Insert some customer data
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
# val = ("John Doe", "john.doe@example.com")

mycursor.execute("""
INSERT INTO customers (name, email)
  VALUES('John Doe', 'john.doe@example.com');                
                 
                 
""")
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

val = ("Jane Smith", "jane.smith@example.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

# Read all customer data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

print("Customers:")
for row in myresult:
  print(row)

# Update a customer's email
sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("updated.email@example.com", 1)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) updated.")

# Read the updated customer data
mycursor.execute("SELECT * FROM customers WHERE id = 1")
myresult = mycursor.fetchone()

print("Updated customer:")
print(myresult)

# Delete a customer
sql = "DELETE FROM customers WHERE id = 2"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

# Close connections
mycursor.close()
mydb.close()

print("Database connection closed.")