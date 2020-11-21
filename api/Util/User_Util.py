from django.contrib.auth.models import User
import string
import secrets

def new_user(username, email, password):
    new_user = User.objects.create_user(username, email, password)

    return new_user

def generate_user_name(name):
    tokens = name.split()
    user_name = tokens[-1]
    for token in tokens[:-1]:
        user_name += token[0]
    return user_name

def generate_password():
    alphabet = string.ascii_letters+string.digits
    return ''.join(secrets.choice(alphabet) for i in range(6))