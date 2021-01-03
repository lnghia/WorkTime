# WorkTime

A simple web application for monitoring employees' workingtime. With the assistance of face recognition, the application can be used widely in offices or schools environment. It provides people the ability to make an attendance without having to touch the same surface like solutions using fingerprint which is very useful during the pandemic like Covid.

## Technologies

- python
- Django
- Django Rest Framework
- Sqlite

## Prerequisites

- python 3.8
- Virtualenv

## Specifications

Out project includes the apis and the graphical web interfaces.

The apis consists of:
- /api/new_worker/ for registering a new employee
- /api/roll_call/ for making an attendace to an employee
- /api/login/ return a token to be used with each api call
- /api/submit-photos/ for feeding portrait images of a new employee
- /api/identify-photo/ for indentifying a portrait image

You can visit the url /api/api_root/ for more information.

## Installation

Download or clone this repos into your machine. All the neccessary modules for the deployment are listed in ```requirements.txt```, just simply execute this command in your shell ```pip install -r requirements.txt``` for the modules installation.

After installing all the needed python modules, you need to make migrations using this command ```python manage.py makemigrations``` then apply all migrations to the database with ```python manage.py migrate```

To grant access to the admin site, you can run ```python manage.py createsuperuser``` and follow the instructions to create a super user account which has the authority to log in the admin site.

You also need to set the email username and password using ```export MAIL_USERNAME=''``` and ```export MAIL_PASSWORD=''```, everytime you create a new worker, an account information email contains a generated password will be sent to the registered email for that worker so you need to set the email username and password to configure a smtp service to do so. ```Remember to use email application password instead of you ordirnary password and you need to do this step after openning a new shell since everytime you close a shell, all the environment variables will be reseted```. 

Execute ```python manage.py runserver``` and you are good to go. If you have any further questions or any ideas to improve our application, just let us know and we'll be very grateful for that. Thank you all ! We are having a hard time during this pandemic, be careful and stay safe, you're not alone in this. Wish you guys all the best !!!


