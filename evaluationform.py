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
class EvaluationForm(FlaskForm):

    #Creates the CourseName field and requires users to use it.
    CourseName=StringField(label="Course Name:",validators=[DataRequired()])

    #Creates the CourseInstructor field and requires users to use it.
    CourseInstructor=StringField(label="Professor Name:",validators=[DataRequired()])
    
    #This creates the radio fields. Coerce makes sure the incoming data is received as an integer!
    CourseScale = RadioField('On a scale of 1 to 5, how would you rate your overall experience in the course?',
                             choices=[(1, '1'), (2, '2'),(3, '3'),(4, '4'),(5, '5')], coerce=int, validators=[DataRequired()])
    
    ProfessorScale = RadioField('On a scale of 1 to 5, how would you rate your overall experience with the professor?',
                             choices=[(1, '1'), (2, '2'),(3, '3'),(4, '4'),(5, '5')], coerce=int, validators=[DataRequired()])
    
    RecommendScale = RadioField('On a scale of 1 to 5, how likely would you recommend this course with the same professor to others?',
                             choices=[(1, '1'), (2, '2'),(3, '3'),(4, '4'),(5, '5')], coerce=int, validators=[DataRequired()])
    
    #Creates the button for users to submit their evaluation form
    Submit=SubmitField(label="Send")

#End of Script
