from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Query

# ------------------- Static Pages -------------------


from django.db.models import Q

from .models import Village

def village_list(request):
    query = request.GET.get('q')
    print('hello')
    if query:
        villages = Village.objects.filter(
            Q(name__icontains=query) |
            Q(district__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(price__icontains=query)
        )
       
        return render(request, 'village_list.html', {'villages': villages, 'query': query})
    else:
        villages = Village.objects.all()
        return render(request, 'village_list.html', {'villages': villages})
    

def village_list1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': user.phone,
        'password': user.password
    }
    msg = 'successfully logged in'

    query = request.GET.get('q')
    print('hello')
    if query:
        villages = Village.objects.filter(
            Q(name__icontains=query) |
            Q(district__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(price__icontains=query)
        )
        
        return render(request, 'village_list.html', {'villages': villages, 'query': query,'msg': msg, 'user': databreak})
    else:
        villages = Village.objects.all()
        return render(request, 'village_list.html', {'villages': villages, 'user': databreak})
   

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


        for i in range(0,10):
            if str(i) in Uname:
                msg = 'name should not contain numbers'
                return render(req, 'register.html', {'msg': msg})  

        if len(phone) != 10:
            msg = 'please enter a valid phone number'
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

        if Eml == 'admin@gmail.com' and Pass1 == 'admin@123':
            request.session['is_admin'] = True
            # Call admin_dashboard directly or redirect
            return redirect('admin_dashboard')

        user = User.objects.filter(email=Eml)
        if user.exists():
            user1 = user.first()
            if user1.password == Pass1:
                # User session set karna bhi zaroori hai agar login session maintain karna ho
                request.session['user_id'] = user1.id
                # normal user dashboard render karna
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



# def logindata(request):
    if request.method == 'POST':
        Eml = request.POST.get('email')
        Pass1 = request.POST.get('password')

        # Static admin login check
        if Eml == 'admin@gmail.com' and Pass1 == 'admin@123':
            admin_data = {
                'id': 0,
                'username': 'Admin',
                'email': Eml,
                'phone': 'N/A',
                'password': '********',
                'profile_image': None
            }
            msg = 'Admin successfully logged in'
            return render(request,  'admin_dashboard.html', {'msg': msg, 'user': admin_data})

        # Normal user login
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
                msg = 'Successfully logged in'
                return render(request, 'dashboard.html', {'msg': msg, 'user': databreak})
            else:
                msg = 'Invalid password'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = 'Email not registered'
            return render(request, 'register.html', {'msg': msg})

    else:
        msg = 'Please fill the form'
        return render(request, 'login.html', {'msg': msg})#
# ------------------- Login with Static Admin -------------------
    

#def logindata(request):
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
        return render(request, 'login.html', {'msg': msg})#

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

#==========================new code====================================
def admin_dashboard(request):
    # Example session check (agar session use karte ho)
    if not request.session.get('is_admin'):
        return redirect('login')

    users = User.objects.all()
    selected_section = None
    if request.method == 'POST':
        selected_section = request.POST.get('action')
    admin_data = {
        'id': 0,
        'username': 'Admin',
        'email': 'admin@gmail.com',
        'phone': 'N/A',
        'password': '********',
        'profile_image': None
    }
 

    return render(request, 'admin_dashboard.html', {
        'user': admin_data,
        'users': users,
        'selected_section': selected_section
        
    })

def logout_view(request):
    request.session.flush()  # clears all session data
    return redirect('login')

#==============================================

def addcard1(request,pk,it):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }
    # print(pk)
    cart = request.session.get('cart',[])
    # print(cart)
    if it in cart:
        msg = "Item already in cart"
        cart = request.session.get('cart',[])
        print(cart)
        cart_items = []
        total = 0
        for i in cart:
          item = Village.objects.get(id=i)
          total += int(''.join(filter(str.isdigit, item.price))) 
          cart_items.append(item)

        return render(request,'cartpage.html', {'cart_items': cart_items, 'total': total,'msg': msg, 'user': databreak})
    else:
        cart.append(it)
        # print(cart)
        request.session['cart']=cart
        msg = "Item added to cart"
        cart = request.session.get('cart',[])
        cart_items = []
        total = 0
        for i in cart:
          item = Village.objects.get(id=i)
          total += int(''.join(filter(str.isdigit, item.price)))
          cart_items.append(item)
        return render(request,'cartpage.html', {'user': databreak,'cart_items': cart_items, 'total': total,'msg': msg,})

       
def remove_from_cart1(request, pk, it):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }
    
    cart = request.session.get('cart', [])
    if it in cart:
        cart.remove(it)
        request.session['cart'] = cart
        msg = "Item removed from cart"
    else:
        msg = "Item not found in cart"

    # Calculate total and prepare cart items
    cart_items = []
    total = 0
    for i in cart:
        item = Village.objects.get(id=i)
        total += int(''.join(filter(str.isdigit, item.price)))
        cart_items.append(item)

    return render(request, 'cartpage.html', {'user': databreak, 'cart_items': cart_items, 'total': total, 'msg': msg})        


#---------------------------------------------------
        
def addcard(request,it):
    cart = request.session.get('cart',[])
    # print(cart)
    if it in cart:
        msg = "Item already in cart"
        cart = request.session.get('cart',[])
        print(cart)
        cart_items = []
        total = 0
        for i in cart:
          item = Village.objects.get(id=i)
          total += int(''.join(filter(str.isdigit, item.price)))
          cart_items.append(item)

        return render(request,'cartpage.html', {'cart_items': cart_items, 'total': total,'msg': msg})
    else:
        cart.append(it)
        # print(cart)
        request.session['cart']=cart
        msg = "Item added to cart"
        cart = request.session.get('cart',[])
        cart_items = []
        total = 0
        for i in cart:
          item = Village.objects.get(id=i)
          total += int(''.join(filter(str.isdigit, item.price)))
          cart_items.append(item)
        return render(request,'cartpage.html', {'cart_items': cart_items, 'total': total,'msg': msg,})

def remove_from_cart(request, it):
    cart = request.session.get('cart', [])
    if it in cart:
        cart.remove(it)
        request.session['cart'] = cart
        msg = "Item removed from cart"
    else:
        msg = "Item not found in cart"

    # Calculate total and prepare cart items
    cart_items = []
    total = 0
    for i in cart:
        item = Village.objects.get(id=i)
        total += int(''.join(filter(str.isdigit, item.price)))
        cart_items.append(item)

    return render(request, 'cartpage.html', {'cart_items': cart_items, 'total': total, 'msg': msg})        




def showcart(request):
    cart = request.session.get('cart', [])
    cart_items = []
    total = 0
    for i in cart:
        item = Village.objects.get(id=i)
        total += int(''.join(filter(str.isdigit, item.price)))
        cart_items.append(item)
    return render(request, 'cartpage.html', {'cart_items': cart_items, 'total': total})    

def showcart1(request, pk):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }
    
    cart = request.session.get('cart', [])
    cart_items = []
    total = 0
    for i in cart:
        item = Village.objects.get(id=i)
        total += int(''.join(filter(str.isdigit, item.price)))
        cart_items.append(item)

    return render(request, 'cartpage.html', {'cart_items': cart_items, 'total': total, 'user': databreak})    

    

from django.shortcuts import render, get_object_or_404
from .models import Village

def village_detail(request, it):
    village = get_object_or_404(Village,id=it)
    return render(request, 'village_detail.html', {'village': village})

def village_detail1(request, pk, it):
    user = User.objects.get(id=pk)
    databreak = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
        'phone': user.phone,
        'profile_image': user.profile_pic
    }
    
    village = get_object_or_404(Village, pk=it)
    return render(request, 'village_detail.html', {'village': village, 'user': databreak})    
