import sqlite3

#Connect to sqlite
connection = sqlite3.connect("student.db")

#Creating a cursor - fore insertion,retrieval,etc
cursor = connection.cursor()

#Creating the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

#Inserting records
cursor.execute('''Insert Into STUDENT values('Siddharth','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Rutuja','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Chhatre','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('KK','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Soham','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Mete','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Kamble','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Roopali','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Aryan','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Riya','DEVOPS','A',35)''')

#Display all the records
print("The inserted records are")
data = cursor.execute('''Select * FROM STUDENT''')

for row in data:
    print(row)

#Closing the connection
connection.commit()
connection.close()