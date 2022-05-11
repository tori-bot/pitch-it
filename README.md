# pitch-it
This is an application to create and present one minute pitches for all kinds of situations. It contains many categories where a user can explore and even configure their own entries. It is the perfect tool to prepare work pitches but also works like a charm in rehearsals for social interaction.
# Author: Victoria Makena

Live link: https://pitches-here.herokuapp.com/

![Pitch It welcome page](app/static/images/welcome.png)
![Pitch It welcome page](app/static/images/screen1.png)

# Features
* A register and login feature for security purposes.
* pitches are saved in a database for future reference.
* User can curate their own profile.

# Behaviour Driven Development
### BEHAVIOUR
The page loads up and gives user options to either login or register an account.
### INPUT
* User fills register form
* User fills login form
* User fills pitch form
* User fills form to update ther profile
### OUTPUT
* User is registered into the application
* User is verified and logged into application
* user's pitch is added to database and is displayed on index page# Setup Instruction
PLease ignore <> when typing commands.

# Setup Instruction
PLease ignore <> when typing commands.

* Clone this repository
* On your terminal type the command: git clone <repo link>
* The project folder is cloned to your local machine
* Activate the virtual environment using command: source pitch/bin/activate
* Install all requirements for the project using the command: pip install -r requirements.txt
* Activate the manage file using command: chmod a+x start.sh
* Run the project on localhost using command: ./start.sh

# Technologies used
Python 3.9.7
Flask 1.1.4
HTML/CSS
Postgresql
SqlAlchemy

For more info on this check the requirements.txt file

# License
Copyright (c) 2022 MIT License. [View License Here](LICENSE)

# Contact Information
Email: makenavictoria1@gmail.com