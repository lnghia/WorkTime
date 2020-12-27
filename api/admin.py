from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import *


# Register your models here.

admin.site.register(LeaveRequest)
admin.site.register(Worker)
admin.site.register(TimeSheet)
admin.site.register(Permission)
admin.site.register(ContentType)