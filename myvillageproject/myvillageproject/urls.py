"""
URL configuration for digital_village_tour project.

The urlpatterns list routes URLs to views. For more information please see:
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




from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.village_list, name='village_list'),
    path('village_list1/<int:pk>', views.village_list1, name='village_list1'),
    path('about', views.about, name='about'),
    path('about1/<int:pk>', views.about1, name='about1'),
    path('register/', views.register, name='register'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('login/', views.login, name='login'),
    path('logindata/', views.logindata, name='logindata'),    
    path('village-life/', views.village_life, name='village_life'),
    path('village-life1/<int:pk>', views.village_life1, name='village_life1'),
    path('Purchase/', views.Purchase, name='Purchase'),
    path('Purchase1/<int:pk>', views.Purchase1, name='Purchase1'),
    path('contact/', views.contact, name='contact'),
    path('contact1/<int:pk>', views.contact1, name='contact1'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('dashboard1/<int:pk>', views.dashboard1, name='dashboard1'), 
    path('profile/', views.profile, name='profile'),
    path('profile1/<int:pk>', views.profile1, name='profile1'),
    path('update/<int:pk>', views.update, name='update'),
    
    # -------------query working----------------    
    path('query/<int:pk>', views.query, name='query'),
    path('allquery/<int:pk>', views.allquery, name='allquery'),
    path('edit_query/<int:pk>/<int:it>/', views.edit_query, name='edit_query'),
    path('delete_query/<int:pk>/<int:it>/', views.delete_query, name='delete_query'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
