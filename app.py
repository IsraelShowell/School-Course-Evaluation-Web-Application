# Creator: Israel Showell
# Start Date: 4/15/2024
# End Date: 4/18/2024
# Project: School-Course-Evaluation System
# Version: 1.40

# Description:
"""
This is a Web application where a user can register an account with a username and password, login into their account, and make an evaluation on a course.
An admin can login and view completed evaluations submitted by users.
This Web application uses SQLite as its database system, HTML/CSS Front-End, and Python as its Back-End. <br>
This Web application is a way for me to practice Flask development, linking HTML/CSS Front-End to Python Back-End, creating a practical program,
reusing old software, and database management actions including, but not limited to; 

- Accessing databases 
- Creating tables inside databases 
- Inserting data into the tables 
- Checking the contents of tables
- Connecting Front-Ends and Back-Ends together
- Developing Web Applications
- Software Reuse
"""

#These are the imported libaries I am using to make the program
#These 2 were used for debugging statements
from __future__ import print_function
import sys

from flask import Flask, render_template, request, session
from registerform import RegistrationForm
from evaluationform import EvaluationForm
from datetime import datetime
import sqlite3
import random



#Important variables and objects
#Requried by Flask to detect the app when running 'flask run'
app = Flask(__name__)
#This is used to help protect data being sent by the app.
#This protection is used to defend against CSRF attacks.
#(Cross-Site Request Forgery)
app.secret_key="__privatekey__"


#All HTML files are located in the 'templates' because that is where render_template looks for HTML files

#The Home Page is located as the root of the web page
@app.route('/')
def Home():
    #Home is referenced in the HTML files
    return render_template('Home.html')


#This is the adminpage
@app.route('/adminpage')
def adminpage():
    #adminpage is referenced in the HTML files
    return render_template('adminpage.html')


#This is the adminview
@app.route('/adminview',methods=['POST','GET'])
def adminview():

    #Gets the current admin's name
    adminname = session.get('adminname')

    #Checks to see if the page is rendered using the POST method
    if request.method=='POST':
            #Gets the user id entered into the box
            user_id = request.form['User_ID']

            if user_id:
                #If the login is right, they go to the admin view page, and their name is displayed along with previous evaluations
                adminviews = sqlite3.connect('Management.db')
                #c serves as a database cursor, a control structure that enables traversal over the records in a database
                a = adminviews.cursor()

                #statement holds an SQL Query for the evaluations table in the management database
                #This query checks to get all evaluations that exist in the database for a certain user
                statement = f"SELECT * FROM evaluations WHERE User_ID='{user_id}' ORDER BY DateEvaluationSubmitted DESC;"

                #We then tell the cursor to run the query
                a.execute(statement)

                #Fetches all the evaluations
                evaluations_from_user = a.fetchall()
    
                #Closes the cursor and database
                a.close()
                adminviews.close()

                newmessage = "These are the submitted evaluations from User_ID: " + user_id + " ordered by date!"
                #Renders the page again
                return render_template('adminview.html', name=adminname, evaluations=evaluations_from_user,message=newmessage)
            
        
    else:
            #This is the default page they see
            #If the login is right, they go to the admin view page, and their name is displayed along with previous evaluations
            adminviews = sqlite3.connect('Management.db')
            #c serves as a database cursor, a control structure that enables traversal over the records in a database
            a = adminviews.cursor()

            #statement holds an SQL Query for the evaluations table in the management database
            #This query checks to get all evaluations that exist in the database
            #This gets the most recent 3 evaluations
            statement=f"SELECT * from evaluations ORDER By DateEvaluationSubmitted DESC LIMIT 3;"

            #We then tell the cursor to run the query
            a.execute(statement)

            #Fetches all the evaluations
            recent_three_evaluations = a.fetchall()
    
            #Closes the cursor and database
            a.close()
            adminviews.close()
            newmessage = "These are the 3 most recent submitted evaluations ordered by date!"
            #Sends the name of the admin and the tuple to adminview.html
            return render_template('adminview.html', name=adminname, evaluations=recent_three_evaluations,message=newmessage)


#This is the adminlogin page
@app.route('/adminlogin',methods=['POST','GET'])
def adminlogin():

    #Checks the page's method
    if request.method=='POST':
        #Saves the request's data in variables
        adminname = request.form['Admin_Username']
        adminpass = request.form['Admin_Password']
        session['adminname'] = adminname
        #Then it connects to the database
        admins = sqlite3.connect('Management.db')
        #c serves as a database cursor, a control structure that enables traversal over the records in a database
        c = admins.cursor()

        #statement holds an SQL Query for the users table in the users database
        #This query checks to see if the user and password entered exist in the database
        statement=f"SELECT * from admins WHERE Admin_Username='{adminname}' AND Password='{adminpass}';"

        #We then tell the cursor to run the query
        c.execute(statement)
        
        #c.fetchone fetchs the next row of a query result and returns a single tuple,
        #Or None if no more rows are available.
        if not c.fetchone():
            #If the adminname and admin password is not found, the program will not sign them in
            return render_template("adminlogin.html")
        else:
            #Closes the database, and heads to the adminview function
            c.close()
            admins.close()

            #These were debug statements I used to fix a GET method error.
            #print(request.method)
            #print("Test!")

            #I brute-forced the request method to fix a bad proxy error. This may cause issues, but for now its fine.
            request.method = 'GET'

            #Returns the adminview function
            return adminview()
        
    elif request.method=='GET':
         #If the user is just going to the login page, the page is rendered by the program
         #adminpage is referenced in the HTML files
         print(request.method)
         return render_template('adminlogin.html')
        
    else:
        #Debug statement
         print(request.method)

#This is the UserPage
@app.route('/userpage')
def userpage():
    #userpage is referenced in the HTML files
    return render_template('userpage.html')

#The Login Page is able to detect POST and GET requests
#POST sends data, GET gets data
@app.route('/login', methods=['POST','GET'])
def login():
    #When the button is pressed, the user makes the page send a POST request
    if request.method=='POST':
        #Saves the request's data in variables
        userName = request.form['Username']
        passWord = request.form['Password']

        #Then it connects to the database
        con = sqlite3.connect('Management.db')
        #c serves as a database cursor, a control structure that enables traversal over the records in a database
        c = con.cursor()

        #statement holds an SQL Query for the users table in the users database
        #This query checks to see if the user and password entered exist in the database
        statement=f"SELECT * from users WHERE Username='{userName}' AND Password='{passWord}';"

        #We then tell the cursor to run the query
        c.execute(statement)
        #c.fetchone fetchs the next row of a query resultand returns a single tuple,
        #Or None if no more rows are available.
        if not c.fetchone():
            #If the user and password is not found, the program will not sign them in
            return render_template("login.html")
        else:
            #If the login is right, the program finds the ID of the user, and fetches it
            statement=f"SELECT User_ID from users WHERE Username='{userName}';"
            c.execute(statement)

            #This gets the ID and removes the comma that is on the end of it
            User_ID = c.fetchone()[0]

            #This detects the stored session name and ID
            session['username'] = userName
            session['user_id'] = User_ID

            #Calls the dashboard function
            return dashboard()
    else:
        #If the user is just going to the login page, the page is rendered by the program
         request.method=='GET'
         return render_template("login.html")

#This is the dashboard function
@app.route('/dashboard') 
def dashboard():
    
    #This detects the stored session name and ID
    username = session.get('username')
    user_id = session.get('user_id')
    
    #This sends the username and id into the dashboard html file
    return render_template("dashboard.html", name = username, UID = user_id)

    

@app.route('/evaluationform', methods=['POST','GET']) 
def evaluationForm():
    #This creates an object named Evaluation based off of the form defined in the registerform module
    Evaluation = EvaluationForm()

    #The program connects to the database
    eva=sqlite3.connect('Management.db')
    #c serves as a database cursor, a control structure that enables traversal over the records in a database
    c=eva.cursor()

    #When the button is pressed, the user makes the page send a POST request
    if request.method=='POST':
        
        #Checks to make sure the user didn't leave the Username and Password fields blank
        if(request.form["CourseName"]!="" and request.form["CourseInstructor"]!="" and request.form["CourseScale"]!="" and request.form["ProfessorScale"]!="" and request.form["RecommendScale"]!=""):
            #Saves the request's data in variables
            CourseName = request.form['CourseName']
            CourseInstructor = request.form['CourseInstructor']
            CourseScale = request.form['CourseScale']
            ProfessorScale = request.form['ProfessorScale']
            RecommendScale = request.form['RecommendScale']
            date_created = datetime.now()
            
            #Generates a random number between 10000 and 30000
            Evaluation_ID = random.randint(10000, 30000)
            
            #statement holds an SQL Query for the evaluations table in the management database
            #This query checks to see if the ID generated exists in the database
            statement=f"SELECT * from evaluations WHERE Eva_ID='{Evaluation_ID}';"

            #We then tell the cursor to run the query
            c.execute(statement)

            #Stores the result of the query in the data variable
            data=c.fetchone()

            #If the data matches ID then the ID will be regenerated
            while data:
                #Generates a random number between 10000 and 30000
                Evaluation_ID = random.randint(10000, 30000)
        
                #statement holds an SQL Query for the evaluations table in the management database
                #This query checks to see if the ID generated exists in the database
                statement=f"SELECT * from evaluations WHERE Eva_ID='{Evaluation_ID}';"

                #We then tell the cursor to run the query
                c.execute(statement)

                #Stores the result of the query in the data variable
                data=c.fetchone()
            
             #If at least the Password or Username are different from what is in the database
            if not data:
                    user_id = session.get('user_id')
                    username = session.get('username')
                    User_ID = user_id
                    Username = username
                    
                    c.execute("INSERT INTO evaluations (Eva_ID,CourseName,CourseInstructor,CourseScale,ProfessorScale,RecommendScale,DateEvaluationSubmitted,User_ID,Username) VALUES (?,?,?,?,?,?,?,?,?)",(Evaluation_ID,CourseName,CourseInstructor,CourseScale,ProfessorScale,RecommendScale, date_created, User_ID,Username))
                    eva.commit()
                    eva.close()
                    
                    #Then they are taken to the login page
                    return render_template("successful.html")
                
    #When a user first goes to the register page, the page is rendered with a fresh form
    elif request.method=='GET':
        return render_template('evaluation.html',form=Evaluation)

    
#The registrationForm Page is able to detect POST and GET requests
#POST sends data, GET gets data
@app.route('/registrationform', methods=['POST','GET']) 
def registrationForm():
    #This creates an object named PingPong based off of the form defined in the registerform module
    Register = RegistrationForm()

    #The program connects to the database
    user=sqlite3.connect('Management.db')
    #c serves as a database cursor, a control structure that enables traversal over the records in a database
    c=user.cursor()

    #When the button is pressed, the user makes the page send a POST request
    if request.method=='POST':
        
        #Checks to make sure the user didn't leave the Username and Password fields blank
        if(request.form["Username"]!="" and request.form["Password"]!=""):
            #Saves the request's data in variables
            userName = request.form['Username']
            passWord = request.form['Password']
            phoneNumber = request.form['PhoneNumber']
            Gender = request.form['Gender']
            Address = request.form['Address']
            Age = request.form['Age']
            date_created = datetime.now()
            
            #statement holds an SQL Query for the users table in the users database
            #This query checks to see if the user and password entered exist in the database
            statement=f"SELECT * from users WHERE Username='{userName}';"

            #We then tell the cursor to run the query
            c.execute(statement)

            #Stores the result of the query in the data variable
            data=c.fetchone()

            #If the data matches both the password and username, then the user will be taken to the error page
            if data:
                return render_template("error.html")
            else:
                #If at least the Username is different from what is in the database
                if not data:
                    
                    #Then the user's username and password will be added into the database
                    #Generates a random number between 10000 and 30000
                    User_ID = random.randint(10000, 30000)

                    #statement holds an SQL Query for the users table in the users database
                    #This query checks to see if the user id generated exists in the database
                    statement=f"SELECT * from users WHERE User_ID='{User_ID}';"

                    #We then tell the cursor to run the query
                    c.execute(statement)
                    
                    #Stores the result of the query in the data variable
                    data2=c.fetchone()

                    #This loop makes sure each ID is unique before adding it to the database
                    while data2:
                        #Then the user's username and password will be added into the database
                        #Generates a random number between 10000 and 30000
                        User_ID = random.randint(10000, 30000)

                        statement=f"SELECT * from users WHERE User_ID='{User_ID}';"

                        #We then tell the cursor to run the query
                        c.execute(statement)
                    
                        #Stores the result of the query in the data variable
                        data2=c.fetchone()

                    c.execute("INSERT INTO users (User_ID,Username,Password,PhoneNumber,Gender,Address,Age,DateAccountCreated) VALUES (?,?,?,?,?,?,?,?)",(User_ID,userName,passWord,phoneNumber,Gender,Address,Age,date_created))
                    user.commit()
                    user.close()
                    
                    #Then they are taken to the login page
                    return render_template("login.html")
                
    #When a user first goes to the register page, the page is rendered with a fresh form
    elif request.method=='GET':
        return render_template('register.html',form=Register)




#This is the start up function that runs when I run flask app in the command line to start the development server
def startup():
    #Connects to the database
    con = sqlite3.connect('Management.db')
    #Sets a cursor to each database
    manage_cursor = con.cursor()
    #Runs a query to create a table if it does not exist
    #The data parameters that the tables can handle are a text username and a text password, etc
    #PRIMARY KEY automatically adds the UNIQUE constraint!
    manage_cursor.execute("CREATE TABLE IF NOT EXISTS users(User_ID INTEGER PRIMARY KEY, Username text NOT NULL, Password text NOT NULL, PhoneNumber INTEGER NOT NULL, Gender text NOT NULL, Address text NOT NULL, Age INTEGER NOT NULL, DateAccountCreated text NOT NULL)")
    manage_cursor.execute("CREATE TABLE IF NOT EXISTS admins(Admin_ID INTEGER PRIMARY KEY, Admin_Username text NOT NULL, Password text NOT NULL, DateAccountCreated text NOT NULL)")

    date_created = str(datetime.now())
    if not manage_cursor.execute("SELECT * FROM admins WHERE Admin_ID = 38721").fetchone():
        #I only need the admin part to run once to make a new admin, that way multiple admins don't exist, thus boosting security
        #I added the comma after the date_created to make sure SQLite recognizes it as a tuple with a single element
        manage_cursor.execute("INSERT INTO admins(Admin_ID, Admin_Username, Password, DateAccountCreated) VALUES(38721, 'admin','admin',?)",(date_created,))
    
    manage_cursor.execute("CREATE TABLE IF NOT EXISTS evaluations(Eva_ID INTEGER PRIMARY KEY, CourseName text NOT NULL, CourseInstructor text NOT NULL, CourseScale INTEGER NOT NULL, ProfessorScale INTEGER NOT NULL,RecommendScale INTEGER NOT NULL, DateEvaluationSubmitted text NOT NULL, User_ID INTEGER NOT NULL, Username text NOT NULL, FOREIGN KEY(User_ID) REFERENCES users(User_ID), FOREIGN KEY(Username) REFERENCES users(Username))")

    #Then the changes are added to the database
    con.commit()


#This needs to be outside of the __name__ part, because Flask skips over it.
startup()
if __name__=='__main__':
    app.run()

#End of Script
