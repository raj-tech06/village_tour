from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Query

# ------------------- Static Pages -------------------

def home(request):
    return render(request, 'home.html')

def home1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password
    }
    msg = 'successfully logged in'
    return render(request, 'home.html', {'msg': msg, 'user': databreak})

# ------------------- About -------------------

def about(request):
    return render(request, 'about.html')

def about1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password
    }
    msg = 'successfully logged in'
    return render(request, 'contact.html', {'msg': msg, 'user': databreak})

# ------------------- Dashboard -------------------

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password,
        'profile_image': user.profile_pic
    }
    msg = 'successfully logged in'
    return render(request, 'dashboard.html', {'msg': msg, 'user': databreak})

# ------------------- Village Life -------------------

def village_life(request):
    return render(request, 'village_life.html')

def village_life1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password
    }
    msg = 'successfully logged in'
    return render(request, 'village_life.html', {'msg': msg, 'user': databreak})

# ------------------- Purchase -------------------

def Purchase(request):
    return render(request, 'Purchase.html')

def Purchase1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password
    }
    msg = 'successfully logged in'
    return render(request, 'Purchase.html', {'msg': msg, 'user': databreak})

# ------------------- Contact -------------------

def contact(request):
    return render(request, 'contact.html')

def contact1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password
    }
    msg = 'successfully logged in'
    return render(request, 'contact.html', {'msg': msg, 'user': databreak})

# ------------------- Register -------------------

def register(request):
    return render(request, 'register.html')

def registerdata(req):
    if req.method == 'POST':
        Uname = req.POST.get('username')
        Eml = req.POST.get('email')
        phone = req.POST.get('phone')
        Pass1 = req.POST.get('password')
        cpass1 = req.POST.get('confirm_password')

        if User.objects.filter(email=Eml).exists():
            msg = 'email already exists'
            return render(req, 'register.html', {'msg': msg})

        if User.objects.filter(username=Uname).exists():
            msg = 'Username already exists'
            return render(req, 'register.html', {'msg': msg})

        if len(Uname) < 6:
            msg = 'please enter your full name'
            return render(req, 'register.html', {'msg': msg})

        if '@' not in Eml or '.' not in Eml or '@.' in Eml or '.@' in Eml:
            msg = 'please enter a valid email'
            return render(req, 'register.html', {'msg': msg})

        if not any(i.isdigit() for i in Pass1):
            msg = 'please make sure your password contains at least one digit'
            return render(req, 'register.html', {'msg': msg})

        if not any(i.isupper() for i in Pass1):
            msg = 'please make sure your password contains at least one upper case letter'
            return render(req, 'register.html', {'msg': msg})

        if not any(i in "!@#$%^&*()-_+={}[]:;'\"<>,.?/" for i in Pass1):
            msg = 'please make sure your password contains at least one special character'
            return render(req, 'register.html', {'msg': msg})

        if len(Pass1) < 8:
            msg = 'password must be at least 8 characters long'
            return render(req, 'register.html', {'msg': msg})

        if Pass1 != cpass1:
            msg = 'password and confirm password are not same'
            return render(req, 'register.html', {'msg': msg})

        User.objects.create(username=Uname, email=Eml, password=Pass1, phone=phone)
        msg = 'successfully registered'
        return render(req, 'login.html', {'msg': msg})

    else:
        msg = 'please fill the form'
        return render(req, 'register.html', {'msg': msg})

# ------------------- Login -------------------

def login(request):
    return render(request, 'login.html')

def logindata(request):
    if request.method == 'POST':
        Eml = request.POST.get('email')
        Pass1 = request.POST.get('password')
        user = User.objects.filter(email=Eml)

        if user.exists():
            user1 = user.first()
            if user1.password == Pass1:
                databreak = {
                    'id': user1.id,
                    'username': user1.username,
                    'email': user1.email,
                    'phone': user1.phone,
                    'password': user1.password,
                    'profile_image': user1.profile_pic
                }
                msg = 'successfully logged in'
                return render(request, 'dashboard.html', {'msg': msg, 'user': databreak})
            else:
                msg = 'invalid password'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = 'Email not registered'
            return render(request, 'register.html', {'msg': msg})

    else:
        msg = 'please fill the form'
        return render(request, 'login.html', {'msg': msg})

# ------------------- Profile -------------------

def profile(request):
    return render(request, 'profile.html')

def profile1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }
    return render(request, 'profile.html', {'user': databreak})

# ------------------- Query -------------------

def query(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }

    if request.method == 'POST':
        name = user.username
        email = user.email
        query_text = request.POST.get('query')

        Query.objects.create(name=name, email=email, query=query_text)
        return render(request, 'dashboard.html', {'user': databreak, 'email': email})

    else:
        msg = 'please fill the form'
        return render(request, 'dashboard.html', {'msg': msg, 'user': databreak})

# ------------------- All Queries -------------------

def allquery(request, pk):
    user = User.objects.get(id=pk)
    print(user.id)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }
    query_data = Query.objects.filter(email=user.email)
    return render(request, 'dashboard.html', {'user': databreak, 'query': query_data})

# ------------------- Edit Query -------------------


from django.shortcuts import render
from django.http import HttpResponse
from .models import Query, User

def edit_query(request, pk, it):
    userdata = User.objects.get(id=pk)
    databreak = {
        'id': userdata.id,
        'username': userdata.username,
        'email': userdata.email,
        'password': userdata.password,
        'phone': userdata.phone,
        'profile_image': userdata.profile_pic
    }

    if request.method == 'POST':
        editdata = Query.objects.get(id=it)
        editdata.query = request.POST.get('query')
        editdata.save()
        return render(request, 'dashboard.html', {'user': databreak, 'editdata': editdata})
    else:
        editquery = Query.objects.get(id=it)
        return render(request, 'dashboard.html', {'user': databreak, 'editquery': editquery})



#-------------for delete query---------------
def delete_query(request, pk, it):
    userdata = User.objects.get(id=pk)
    databreak = {
        'id': userdata.id,
        'username': userdata.username,
        'email': userdata.email,
        'password': userdata.password,
        'phone': userdata.phone,
        'profile_image': userdata.profile_pic
    }
    
    query = Query.objects.get(id=it)
    query.delete()

    return render(request, 'dashboard.html', {'user': databreak})







# ------------------- Update Profile form -------------------

def update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.profile_pic = request.FILES.get('profile_image')
        user.username = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.password = request.POST.get('password')
        user.save()
        msg = 'successfully updated'
        databreak = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'phone': user.phone,
            'profile_image': user.profile_pic
        }
        return render(request, 'dashboard.html', {'msg': msg, 'user':databreak})


