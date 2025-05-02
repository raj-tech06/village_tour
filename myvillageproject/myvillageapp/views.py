from django.shortcuts import render, redirect,HttpResponse

from .models import User


# ------------------- Static Pages -------------------

def home(request):
    return render(request, 'home.html')

def home1(request,pk):
    user=User.objects.get(id=pk)
    databreak={
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'phone': user.phone,
                'password':user.password
              }

    msg='successfully logged in'
    return render(request,'home.html',{'msg':msg, 'user':databreak})

# -------------------------------------home end--------------------------

def about(request):
    return render(request, 'about.html')

def about1(request,pk):
    user=User.objects.get(id=pk)
    databreak={
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'phone': user.phone,
                'password':user.password
              }
    msg='successfully logged in'
    return render(request,'dashboard.html',{'msg':msg, 'user':databreak})


# -------------------------------------about end--------------------------


def dashboard(request):
    msg = 'login 1st!'
    return render(request, 'dashboard.html',{'msg': msg})

def dashboard1(request,pk):
        user=User.objects.get(id=pk)
        databreak={
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'phone': user.phone,
            'password':user.password
        }
        msg='successfully logged in'
        return render(request,'dashboard.html',{'msg':msg, 'user':databreak})
            
            
# -------------------------------------dashboard end--------------------------


def village_life(request):
    return render(request, 'village_life.html')

def village_life1(request,pk):
        user=User.objects.get(id=pk)
        databreak={
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'phone': user.phone,
            'password':user.password
        }
        msg='successfully logged in'
        return render(request,'dashboard.html',{'msg':msg, 'user':databreak})
            

# -------------------------------------village_life end--------------------------

def festivals(request):
    return render(request, 'festivals.html')

def festivals1(request,pk):
        user=User.objects.get(id=pk)
        databreak={
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'phone': user.phone,
            'password':user.password
        }
        msg='successfully logged in'
        return render(request,'dashboard.html',{'msg':msg, 'user':databreak})
            
# -----------------------------------fastivals end--------------------------
def contact(request):
    return render(request, 'contact.html')

def contact1(request,pk):
        user=User.objects.get(id=pk)
        databreak={
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'phone': user.phone,
            'password':user.password
        }
        msg='successfully logged in'
        return render(request,'dashboard.html',{'msg':msg, 'user':databreak})
            
# -----------------------------------contact end--------------------------


def register(request):
    return render(request, 'register.html')

def registerdata(req):
    if req.method == 'POST':

        # fname=req.POST.get('full_name')
        Uname=req.POST.get('username')
        Eml=req.POST.get('email')
        Pass1=req.POST.get('password')
        cpass1=req.POST.get('confirm_password')

        # check for empty fields
        user=User.objects.filter(email=Eml)
        if user:
            msg='email already exists'
            return render(req,'register.html',{'msg':msg})
        
        # check for username
        user_username = User.objects.filter(username=Uname)
        if user_username:
            msg = 'Username already exists'
            return render(req, 'register.html', {'msg': msg})
                

        else:

            if len(Uname)<6:
                msg='please enter your full name' 
                return render(req,'register.html',{'msg':msg})
            
            if "@" not in Eml or "." not in Eml:
                msg='please enter a valid email'
                return render(req,'register.html',{'msg':msg})
            if "@." in Eml or ".@" in Eml:
                msg='please enter a valid email'
                return render(req,'register.html',{'msg':msg})
            

            checker=False
            # check for digit
            for i in Pass1:
                if i.isdigit():
                    checker=True
                    break
            
            if(checker==False):
                msg='please make sure your password contains at least one digit'        
                return render(req,'register.html',{'msg':msg})    
            checker=False

            # check for upper case
            for i in Pass1:
                if i.isupper():
                    checker=True
                    break   
            if(checker==False):
                msg='please make sure your password contains at least one upper case letter'        
                return render(req,'register.html',{'msg':msg})

            checker=False 
            spchar="!@#$%^&*()-_+={}[]:;'\"<>,.?/"
            for i in Pass1:
                if i in spchar:
                    checker=True
                    break
                    

            if(checker==False):
                msg='please make sure your password contains at least one special character'        
                return render(req,'register.html',{'msg':msg})    
                
            if len(Pass1)<8:
                msg='please must be cahrater length 8'
                return render(req,'register.html',{'msg':msg})
            
            if Pass1!=cpass1:
                msg='password and confirm password are not same'
                return render(req,'register.html',{'msg':msg})
            
            else:
                User.objects.create(username=Uname,email=Eml,password=Pass1)
                msg='successfully registered'
                return render(req,'login.html',{'msg':msg})


    else:
        msg='please fill the form'
        return render(req,'register.html',{'msg':msg})

# -----------------------------------register end--------------------------


def login(request):
    return render(request, 'login.html')


        
def logindata(request):
    if request.method == 'POST':
        Eml=request.POST.get('email')
        Pass1=request.POST.get('password')

        user=User.objects.get(email=Eml)
        if user:
            if user.password==Pass1:
                databreak={
                    'id': user.id,
                    'username':user.username,
                    'email':user.email,
                    'phone': user.phone,
                    'password':user.password
                }
                msg='successfully logged in'
                return render(request,'dashboard.html',{'msg':msg, 'user':databreak})
            else:
                msg='invalid password'
                return render(request,'login.html',{'msg':msg})
        else:
            msg='invalid username or password'
            return render(request,'login.html',{'msg':msg})
    else:
        msg='please fill the form'
        return render(request,'login.html',{'msg':msg})


# -----------------------------------login end--------------------------


def profile(request):
    return render(request, 'profile.html')

        
def profile1(request,pk):
    user=User.objects.get(id=pk)
    databreak={
                    'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    'password':user.password
                }

    return render(request, 'profile.html',{'user':databreak})


#   ------------------- Profile end -------------------
