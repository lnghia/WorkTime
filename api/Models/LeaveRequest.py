from django.db import models
from .TimeSheet import TimeSheet
from .Worker import Worker

class LeaveRequest(models.Model):
    worker = models.ForeignKey(Worker, related_name='leave_request', on_delete=models.CASCADE)
    time_sheet = models.OneToOneField(TimeSheet, related_name='leave_request', on_delete=models.CASCADE)
    leave_from = models.TimeField(blank=False)
    leave_to = models.TimeField(blank=False)
    approved = models.BooleanField(default=False)

    # class Meta:
    #     permissions = (
    #         ('add_leaverequest', 'Can add leave request'),
    #         ('change_leaverequest', 'Can change leave request'),
    #         ('delete_leaverequest', 'Can delete leave request'),
    #         ('view_leaverequest', 'Can view leave request')
    #     )