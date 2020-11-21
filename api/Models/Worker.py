# from api.Util.User import new_user
from api.Util.User_Util import new_user
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ..Util import User_Util
import secrets
import string
from datetime import date, datetime

class Worker(models.Model):
    name = models.CharField(max_length=50, blank=False)
    # image = models.ImageField(upload_to='worker_images/', max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, unique=True)

    @staticmethod
    def create_account(email):
        username = email
        password = User_Util.generate_password()
        new_user = User_Util.new_user(username, email, password)
        return username, password, new_user

    @staticmethod
    def is_email_unique(email):
        return Worker.objects.get(email=email) is None

    @staticmethod
    def does_id_exist(id):
        return len(Worker.objects.filter(id=id))

    def make_roll_call(self):
        today = datetime.today().strftime('%Y-%m-%d')
        
        today_shift = self.time_sheet.filter(date=today)

        if not len(today_shift):
            self.time_sheet.create()
        else:
            today_shift[0].work_out = datetime.now().time()
            today_shift[0].save()