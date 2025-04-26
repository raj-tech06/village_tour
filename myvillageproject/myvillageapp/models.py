from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username





















































# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver





# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pics/', default='default-avatar.png')
#     bio = models.TextField(blank=True)
#     email = models.EmailField(blank=True, null=True)  # 👈 Add this line
#     full_name= models.TextField(blank=True)

#     # def __str__(self):
#     #     return self.user.username


# # Signal to automatically create/update user profile
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()


# from django.db import models

# class Tour(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     location = models.CharField(max_length=100)
#     date = models.DateField()
#     full_name= models.TextField(blank=True)


#     def __str__(self):
#         return self.name
