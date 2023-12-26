from django.db import models
from django.shortcuts import redirect


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class signupmodel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    def password(self):
        if self.password1 == self.password2:
            pass
        else:
            return redirect(signupmodel)