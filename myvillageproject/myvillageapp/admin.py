from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import Tour

# admin.site.register(Tour)
from django.contrib import admin
from .models import User, Query, Village
admin.site.register(User)
admin.site.register(Query)
admin.site.register(Village)
