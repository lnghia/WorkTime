from django.db.models import fields
from rest_framework import serializers
from ..Models import Worker
from ..Util.Email_Util import send_email

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['name', 'email']
