import mysql.connector 

dom = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password ='WJ28@krhps',
  database =  'dom'
)

mycursor = dom.cursor()

mycursor.execute("""

SELECT * FROM Sub;


""")


myresult = mycursor.fetchall()






dom.commit()
mycursor.close()
dom.close()

for row in myresult:
  print(row)