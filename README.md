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

## Installation

Download or clone this repos into your machine. All the neccessary modules for the deployment are listed in ```requirements.txt```, just simply execute this command in your shell ```pip install -r requirements.txt``` for the modules installation.

After installing all the needed python modules, you need to make migrations using this command ```python manage.py makemigrations``` then apply all migrations to the database with ```python manage.py migrate```

Finally, just execute ```python manage.py runserver``` and you are good to go. If you have any further questions or any ideas to improve our application, just let us know and we'll be very grateful for that. Thank you all ! We are having a hard time during this pandemic, be careful and stay safe, you're not alone in this. Wish you guys all the best !!!
