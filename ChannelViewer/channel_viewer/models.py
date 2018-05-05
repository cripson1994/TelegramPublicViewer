# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True, default='test')

class UserChannels(models.Model):
    userid = models.ForeignKey(User,  on_delete=models.CASCADE)
    channelid = models.ForeignKey(Channel,  on_delete=models.CASCADE)