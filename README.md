# Creator: Israel Showell
# Start Date: 4/15/2024
# End Date: 4/18/2024
# Project: School-Course-Evaluation System
# Version: 1.40

# Description:
This is a Web application where a user can register an account with a username and password, login into their account, and make an evaluation on a course.
An admin can login and view completed evaluations submitted by users.
This Web application uses SQLite as its database system, HTML/CSS Front-End, and Python as its Back-End. <br>
This Web application is a way for me to practice Flask development, linking HTML/CSS Front-End to Python Back-End, creating a practical program,
reusing old software, and database management actions including, but not limited to; 

- Database documentation
- Accessing databases 
- Creating tables inside databases 
- Inserting data into the tables 
- Checking the contents of tables
- Connecting Front-Ends and Back-Ends together
- Developing Web Applications
- Software Reuse; Primialy Component and Unit reuse

# Note:
Reused code from my previous repo: <br>
https://github.com/IsraelShowell/Register-Login-Website

# Version History:
# V-1.00: (4-15-18-24)
Initial Version <br>
Uploaded to Github <br>

# Version History:
# V-1.10: (4-22-23-24)
Evaluations now save the id of the user who submitted it <br>
Updated various functions to allow for smoother passing of variables and data <br>

# Version History:
# V-1.20: (4-23-24)
Web application is now available online: <br>
https://sisrael.pythonanywhere.com/

# Version History:
# V-1.30: (4-26-24)
Modified the database's fields to include more information and improve readability <br>
Evaluations now show the user's name who submitted it

# Version History:
# V-1.40: (5-1-24)
Modified the database's fields to improve readability <br>
An admin can now choose to view the most recent 3 evaluations or look up a specific user's ID <br>
Improved the UI for the AdminView page <br>
Added better password security for login pages <br>
Added database documentation


# Current Features as of V-1.40:
- A user can create an account, login into it, and create an evaluation on a course and its instructor and submit the evaluation to the database
- An admin can sign into their account, and view the 3 most recent submitted evaluations
- An admin can also look up a user's ID and see all evaluations they have submitted
- Database and its tables can be easily changed to allow for changes and updates
- Multiple sessions can now be supported and done at once
- Web application is accessible online
- Database documentation is now added to showcase the flow of the application

# Future Features to Implement:
- Allow online access to users; Done!
- Improve the UI; AdminView page improved
- Allow more evaluations viewing methods; Done!
- Refactor code; In progress

# Known/Possible Bugs:
- Forced a method to switch to GET in a function, may cause errors, but so far none have been detected
