from django.db import models
from django.contrib.auth.models import AbstractUser


OCCUPATION = [
    ("pm", "PM"),
    ("design", "Design"),
    ("web", "Web"),
    ("ios", "iOS"),
    ("android", "Android"),
    ("server", "Server"),
]


class User(AbstractUser):
    occupation = models.CharField(choices=OCCUPATION, default="", max_length=10)

    def __str__(self):
        return f"이름 : {self.email}/ 직군: {self.occupation}"
