from django.core.exceptions import ValidationError
from rest_framework import serializers
from ..models import Worker

class RollCallSerializer(serializers.BaseSerializer):

    def to_internal_value(self, data):
        id = data.get('id')

        if not id:
            raise serializers.ValidationError('This field is required.')

        if not isinstance(id, int):
            raise serializers.ValidationError('This field must be an integer.')

        if not Worker.does_id_exist(id):
            raise serializers.ValidationError('This object id doesn\'t exist.')

        return {
            'id': data['id']
        }

    def to_representation(self, value):
        return {
            'id': value.id
        }