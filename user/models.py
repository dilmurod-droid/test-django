from django.contrib.auth.models import AbstractUser
from django.db import models

from tests.models import Question


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('mentor', 'Mentor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')