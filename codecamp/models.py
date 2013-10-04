import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import UserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
		 	username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    username = models.CharField(max_length=200, unique=True, db_index=True, null=True)
    email = models.EmailField(max_length=254, db_index=True, null=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, db_index=True)
    name = models.CharField(max_length=50)

    objects = MyUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def __unicode__(self):
        return self.email or self.name or ''


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
