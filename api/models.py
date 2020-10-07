from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, username, usertype, password=None):
        if not username:
            raise ValueError('username must be set!')
        if not usertype:
            raise ValueError('usertype must be set!')

        user = self.model(username=username, usertype=usertype)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, usertype, password=None):
        user = self.create_user(username=username, usertype=usertype, password=password)
        user.is_admin = True
        user.save(using=self._db)

        return user


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(AbstractBaseUser):
    userTypes = [
        ('ST', 'STUDENT'),
        ('TE', 'TEACHER'),
        ('OW', 'OWNER'),
        ('AD', 'ADMIN')
    ]

    username = models.CharField(max_length=15, unique=True)
    usertype = models.CharField(max_length=2, choices=userTypes, default='ST')
    password = models.CharField(max_length=25)
    is_admin = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ['usertype']
    USERNAME_FIELD = 'username'

    objects = AccountManager()

    def __dir__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    front = models.CharField(max_length=200)
    back = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return '(' + self.lesson.name + ') ' + self.front + " " + self.back
