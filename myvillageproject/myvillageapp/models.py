from django.db import models

class User(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpeg/*', blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.username
    
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()
    
    def __str__(self):
        return self.name    

from django.db import models

class Village(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='villages/')
    distance = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

