from django.db import models
from admins1.models import Products


# Create your models here.
class Register(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)
    cmobile = models.CharField(max_length=50)
    caddress = models.CharField(max_length=50)
    cpincode = models.CharField(max_length=50)


class Login(models.Model):
    EMAIL = models.CharField(max_length=50)
    PASSWORD = models.CharField(max_length=50)


class Purchase(models.Model):
    pname = models.CharField(max_length=50)
    pcat = models.CharField(max_length=50)
    pcost = models.CharField(max_length=50)
    pquality = models.CharField(max_length=50)
    pdec = models.CharField(max_length=50)
    cid = models.ForeignKey(Register, on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)
