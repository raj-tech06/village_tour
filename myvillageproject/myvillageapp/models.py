from django.db import models

class User(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpeg', blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10) 
    
    def __str__(self):
        return self.username
    
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()
    
    def __str__(self):
        return self.name    
