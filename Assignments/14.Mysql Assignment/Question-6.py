# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

#ans)

import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user ='abc', password = 'password')
print("Connection with data base established")
mycursor = mydb.cursor()
mycursor.execute("Show databases")
mydb.close()


'''
Cursor() is a pointer to specify the from where action to be take in the data base environment. 

execute()

This method accepts a MySQL query as a parameter and executes the given query.

'''