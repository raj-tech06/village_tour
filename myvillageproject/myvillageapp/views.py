from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
import re

# ------------------- Static Pages -------------------

def home(request):
    return render(request, 'home.html')

def village_life(request):
    return render(request, 'village_life.html')

def gallery(request):
    return render(request, 'gallery.html')

def festivals(request):
    return render(request, 'festivals.html')

def contact(request):
    return render(request, 'contact.html')

# ------------------- Auth -------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is None:
            return render(request, 'login.html', {'error': 'Invalid User'})
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error1': 'Invalid Password'})
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if len(username) < 4 or not re.search(r'\d', username) or len(username) < 8:
            messages.error(request, "Username must be at least 8 characters and contain a number.")
            return render(request, 'register.html')

        if len(password) < 8 or password != confirm_password:
            messages.error(request, "Password must be at least 8 characters and match confirmation.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login') 

    return render(request, 'register.html')

# ------------------- Dashboard -------------------

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


# ------------------- Profile -------------------

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        # Update username
        new_username = request.POST.get('user')
        if new_username and new_username != request.user.username:
            request.user.username = new_username
            request.user.save()


        # Update email
        new_username = request.POST.get('email')
        if new_username and new_username != request.user.email:
            request.user.email = new_username
            request.user.save()


        # Update profile picture
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
            profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('profile')

    # return render(request, 'update_profile.html', {'profile': profile})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User

@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        # Update username
        new_username = request.POST.get('user')
        if new_username and new_username != request.user.username:
            request.user.username = new_username
            request.user.save()

        # Update email
        new_email = request.POST.get('email')
        if new_email and new_email != request.user.email:
            request.user.email = new_email
            request.user.save()

        # Update profile picture
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
            profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('profile')

    return render(request, 'view_profile.html', {'profile': profile})




@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        user = request.user
        user = request.email

        user.username = request.POST.get('user')
        user.email = request.POST.get('email')

        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

        user.save()
        profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('profile')

    return render(request, 'update_profile.html', {'profile': profile})
