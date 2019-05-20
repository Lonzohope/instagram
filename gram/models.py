# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Profile(models.Model):
   profile_photo = models.ImageField(upload_to=)
   bio = models.CharField(max_length =30)


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    image_profile = models.ForeignKey(Profile)
    image_comments =  models.CharField(max_length =30)
    image_likes = models.IntegerField


