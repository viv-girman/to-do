from django.db import models
from django.contrib.auth.models import AbstractUser

from app.utils import mobile_number_validator


class User(AbstractUser):
    email = models.EmailField(("email address"), unique=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def Meta():
        db_table = "user"


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def Meta():
        db_table = "todo"
