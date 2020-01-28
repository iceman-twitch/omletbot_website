from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    id = models.AutoField(primary_key=True)
    ft_follow   = models.CharField(max_length=120,default='NULL')
    ft_view   = models.CharField(max_length=120,default='NULL')
    ft_like   = models.CharField(max_length=120,default='NULL')
    follow   = models.CharField(max_length=120,default='NULL')
    view   = models.CharField(max_length=120,default='NULL')
    like   = models.CharField(max_length=120,default='NULL')

# # Create your models here.
# class FreeTrialFollow(models.Model):
#     id = models.AutoField(primary_key=True)
#     username   = models.CharField(max_length=120,default='NULL')
#     time   = models.CharField(max_length=120,default='NULL')
    
# # Create your models here.
# class FreeTrialView(models.Model):
#     id = models.AutoField(primary_key=True)
#     username   = models.CharField(max_length=120,default='NULL')
#     time   = models.CharField(max_length=120,default='NULL')
    

class Bots(models.Model):
    id = models.AutoField(primary_key=True)
    username   = models.CharField(max_length=120,default='NULL')
    kind        = models.IntegerField(default=0)
    name        = models.CharField(max_length=120,default='NULL')
    time   = models.CharField(max_length=120,default='NULL')

class Queue(models.Model):
    username   = models.CharField(max_length=120,default='NULL',unique=True)
    kind        = models.IntegerField(default=0)
    time   = models.CharField(max_length=120,default='NULL')
class Proxies(models.Model):
    proxy= models.CharField(max_length=120,unique=True,null=False)
    active = models.BooleanField(default=True)
class Count(models.Model):
    name=models.CharField(max_length=120,unique=True,null=False)
    count=models.IntegerField(null=False,default=0)