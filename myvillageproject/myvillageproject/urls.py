"""
URL configuration for digital_village_tour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.urls import path
from myvillageapp import views




# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('login/', views.login, name='login'),
    path('logindata/', views.logindata, name='logindata'),    
    # path('village-life/', views.village_life, name='village_life'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('festivals/', views.festivals, name='festivals'),
    # path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('profile/', views.profile, name='profile'),
    path('profile1/<int:pk>', views.profile1, name='profile1'),

    # path('profile/update/', views.update_profile, name='update_profile'),


] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


