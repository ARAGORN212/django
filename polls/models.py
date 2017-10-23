# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Db(models.Model):
    user = models.IntegerField()
    film = models.IntegerField()
    rate = models.IntegerField()
