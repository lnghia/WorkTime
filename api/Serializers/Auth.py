from django.db.models import fields
from rest_framework import serializers

class LoginSerializer(serializers.BaseSerializer):
    fields = [
        'username',
        'password',
    ]
    
    def to_internal_value(self, data):
        username = data.get('username')
        password = data.get('password')

        errors = {}
        messages = {}
        validation_msgs = {}
        validation_err = False

        for field in self.fields:
            errors[field] = False
            messages[field] = []

        if username is None:
            errors['username'] = True
            messages['username'].append('This field is required.')
        if password is None:
            errors['password'] = True
            messages['password'].append('This field is required.')

        for e in errors:
            if errors[e]:
                validation_err = True
                validation_msgs[e] = messages[e]

        if validation_err:
            raise serializers.ValidationError(validation_msgs)

        return {
            'username': username,
            'password': password
        }