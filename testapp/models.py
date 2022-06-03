from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defalut.png' , upload_to='profile_pics' )
    age = models.IntegerField()
    phone = models.IntegerField(null= True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.SmallIntegerField()


    def __str__(self):
        return self.user.username

