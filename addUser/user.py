import mysql.connector
import cgi

form = cgi.FieldStorage() #get form data

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="python_bsc"
)