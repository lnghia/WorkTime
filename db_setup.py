from django.contrib.auth.models import Group, Permission
from api.models import Worker, TimeSheet, LeaveRequest
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

manager, created = Group.objects.get_or_create(name='manager')
worker, created = Group.objects.get_or_create(name='worker')

worker_ct = ContentType.objects.get(model='worker', app_label='api')
timesheet_ct = ContentType.objects.get(model='timesheet', app_label='api')
leave_ct = ContentType.objects.get(model='leaverequest', app_label='api')	

manager.permissions.add(Permission.objects.get(codename='add_worker'))
manager.permissions.add(Permission.objects.get(codename='change_worker'))
manager.permissions.add(Permission.objects.get(codename='delete_worker'))
manager.permissions.add(Permission.objects.get(codename='view_worker'))
manager.permissions.add(Permission.objects.get(codename='add_timesheet'))
manager.permissions.add(Permission.objects.get(codename='view_timesheet'))
manager.permissions.add(Permission.objects.get(codename='add_leaverequest'))
manager.permissions.add(Permission.objects.get(codename='change_leaverequest'))
manager.permissions.add(Permission.objects.get(codename='delete_leaverequest'))
manager.permissions.add(Permission.objects.get(codename='view_leaverequest'))

worker.permissions.add(Permission.objects.get(codename='view_timesheet'))
worker.permissions.add(Permission.objects.get(codename='view_leaverequest'))




	
