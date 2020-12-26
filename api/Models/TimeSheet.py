from django.db import models
from .Worker import Worker

class TimeSheet(models.Model):
    worker = models.ForeignKey(Worker, related_name='time_sheet', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    work_in = models.TimeField(auto_now_add=True)
    work_out = models.TimeField(blank=True, null=True)

    # class Meta:
    #     permissions = (
    #         ('add_timesheet', 'Can add time sheet'),
    #         ('change_timesheet', 'Can change time sheet'),
    #         ('delete_timesheet', 'Can delete time sheet'),
    #         ('view_timesheet', 'Can view time sheet')
    #     )