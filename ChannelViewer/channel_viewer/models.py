# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
	#usr = models.ForeignKey(User,  on_delete=models.CASCADE)
	#usr = models.ManyToManyField(User)
    name = models.CharField(max_length=128, null=False, blank=False, unique=True, default='test')

class Photo(models.Model):
    pass
	#frl = models.ForeignKey(Channel,  on_delete=models.CASCADE)
	#frl = models.ManyToManyField(Channel)