from getpass import getpass 
import mysql.connector 

dom = mysql.connector.connect(
  host = "localhost",
  user = 'root',
  password = 'WJ28@krhps',
  database = 'dom'
)


print(dom.get_server_info())


mycursor = dom.cursor()

mycursor.execute("""
CREATE TABLE Sub
(PositionID INT PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50)
);
""")

mycursor.execute("DESCRIBE TABLE Sub;")
myresult = mycursor.fetchall()

dom.commit()
mycursor.close()
dom.close()

print(myresult)