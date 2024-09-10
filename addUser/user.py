import mysql.connector

#connect to the MYSQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="python_bsc"
)

#create a cursor object for interacting with a MySQL database through the mysql.connector module.
cursor = db.cursor()

#User class store userName and password
class User:
  def __init__(self, userName, password):
    self.userName = userName
    self.password = password

def getUserInputs():
    #get input values
    userName = input("Enter your Email : ")
    password = input("Enter your Password : ")
    #return User object
    return User(userName, password)
     

def saveUser():
    #get user input as an user object
    user = getUserInputs()
    
    print(user.userName)
    print(user.password)
    
    #insert user data into database
    try:
        query = "INSERT INTO users (userName, password) VALUES (%s, %s)"
        cursor.execute(query, (user.userName, user.password))
        db.commit()
        print("User Added Successfully !")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # close connection and cursor
        cursor.close()
        db.close()
        
saveUser()