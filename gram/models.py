from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to =30)
    bio = models.CharField(max_length =30)
    
    def __str__(self):
      return self.name

    def save_profile(self):
        self.save()
   

class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    image_profile = models.ForeignKey(Profile)
    image_comments =  models.CharField(max_length =30)
    image_likes = models.IntegerField
   

    def __str__(self):
      return self.image_name

    class Meta:
        ordering = ['image']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.save()

    def update_caption(self):
        self.caption()

    @classmethod
    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images
        
    @classmethod
    def search_by_image_profile(cls,search_item):
        images = cls.objects.filter(image_icontains=search_term)
        return images

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


class Index(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    article_image = models.ImageField(upload_to='index/', blank=True)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=140)
    last_login = models.DateTimeField(auto_now=True)
    