from django.db import models
# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=255)
    login_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=6)
    avatar = models.CharField(max_length=255)

    def __str__(self):
        return self.name +  " " + self.email + " " + self.type + " " + self.avatar
