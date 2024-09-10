import mysql.connector
import cgi

form = cgi.FieldStorage() #get form data

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="python_bsc"
)

#create a cursor object for interacting with a MySQL database through the mysql.connector module.
cursor = db.cursor()

#get input values
userName = form.getvalue("userName")
password = form.getvalue("password")

#insert user data into database
try:
    query = "INSERT INTO users (userName, password) VALUES (%s, %s)"
    cursor.execute(query, (userName, password))
    db.commit()
    print("Content-type:text/html\r\n\r\n")
    print("<html><body><h2>User added successfully!</h2></body></html>")