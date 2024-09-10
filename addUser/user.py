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