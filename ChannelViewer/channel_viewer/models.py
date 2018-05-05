# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
	usr = models.ForeignKey(User,  on_delete=models.CASCADE)

class Photo(models.Model):
	frl = models.ForeignKey(Channel,  on_delete=models.CASCADE)