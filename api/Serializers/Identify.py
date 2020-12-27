from django.core.exceptions import ValidationError
from rest_framework import serializers
from ..Models import Worker

class SubmitPhotoSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        id = data.get('id')

        if not id:
            raise serializers.ValidationError('This field is required.')

        if not isinstance(id, int):
            raise serializers.ValidationError('This field must be an integer.')

        if not Worker.does_id_exist(id):
            raise serializers.ValidationError('This object id doesn\'t exist.')

        directions_images = ['left', 'front', 'right']

        for key in directions_images:
            if not data[key]:
                raise serializers.ValidationError('This field is required.')

            if not isinstance(data[key], str):
                raise serializers.ValidationError('This field must be a base64 encoded photo.')

        return {
            'id': data['id'],
            'left': data['left'],
            'front': data['front'],
            'right': data['right']
        }

    def to_representation(self, value):
        return {
            'id': value.id,
            'left': value.left,
            'front': value.front,
            'right': value.right
        }

class PredictPhotoSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        image = data.get('image')

        if not image:
            raise serializers.ValidationError('This field is required.')

        if not isinstance(image, str):
            raise serializers.ValidationError('This field must be a base64 encoded photo.')

        return {
            'image': image
        }

    def to_representation(self, value):
        return {
            'image': value.image
        }