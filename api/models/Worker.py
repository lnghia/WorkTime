# from api.Util.User import new_user
from rest_framework.authtoken.models import Token
from api.Util.User_Util import new_user
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ..Util import User_Util
import secrets
import string
from datetime import date, datetime
import datetime as dt
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate


class Worker(models.Model):
    name = models.CharField(max_length=50, blank=False)
    # image = models.ImageField(upload_to='worker_images/', max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, unique=True)
    start_of_month = models.DateField(blank=True, null=True, auto_now_add=True)

    # class Meta:
    #     permissions = (
    #         ('make_rollcall', 'Can make a roll call.')
    #     )

    @staticmethod
    def create_account(email):
        worker_group = Group.objects.get(name='worker')
        username = email
        password = User_Util.generate_password()
        new_user = User_Util.new_user(username, email, password)
        worker_group.user_set.add(new_user)
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

    def verify_password(self, password):
        return authenticate(username=self.email, password=password) is not None

    def generate_token(self):
        token, created = Token.objects.get_or_create(user=self.user)
        return token

    def day_num_since_start_of_month(self, d2):
        d1 = self.start_of_month
        return (d2-d1).days

    def update_start_of_month(self, curr_date):
        # print(self.day_num_since_start_of_month(curr_date))
        if self.day_num_since_start_of_month(curr_date) > 28:
            self.start_of_month += dt.timedelta(days=28)
            self.save()
