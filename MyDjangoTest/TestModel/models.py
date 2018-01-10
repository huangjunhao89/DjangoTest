# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.ImageField()
    address = models.CharField(max_length=20)
    data = models.DateField()

class User(models.Model):
    user = models.CharField(max_length=20)
    password =  models.CharField(max_length=20)


