# Creator: Israel Showell
# Start Date: 4/15/2024
# End Date: 4/18/2024
# Project: School-Course-Evaluation System
# Version: 1.20

# Description:
"""
This will be a Web application where a user can register an account with a username and password, login into their account, and make an evaluation on a course.
An admin will be able to login and view completed evaluations submitted by users.
This is a Web application uses SQLite as its database system, HTML/CSS Front-End, and Python as its Back-End. <br>
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
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,IntegerField,TextAreaField,SubmitField
from wtforms.validators import ValidationError, DataRequired
from wtforms import RadioField

#Here, I create a form format that will be rendered by app.py and by the HTML page
class RegistrationForm(FlaskForm):
    #Creates the username field and requires users to use it.
    Username=StringField(label="Username",validators=[DataRequired()])
    #Creates the password field and requires users to use it.
    Password=PasswordField(label="Password",validators=[DataRequired()])
    #Creates the phone field and requires users to use it.
    PhoneNumber=IntegerField(label="Enter Mobile Number",validators=[DataRequired()])
    #Creates the Gender field 
    Gender=StringField(label="Gender")
    #Creates the address TextAreaField 
    Address=TextAreaField(label="Address")
    #Creates the username field and requires users to use it.
    Age=IntegerField(label="Age")
    
    #Creates the button for users to submit their form
    Submit=SubmitField(label="Send")

#End of Script
