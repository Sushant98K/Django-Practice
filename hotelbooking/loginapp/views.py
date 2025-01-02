from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import *
from userapp.models import *


def login(request):
    if request.method == 'POST':
        type = request.POST['type']
        email = request.POST['email']
        password = request.POST['password']
        
        if type == 'user':
            cust = User.objects.get(email=email)
            if cust:
                flag = check_password(password, cust.password)
                if flag:
                    
                    return HttpResponse("<h1>User Log In successful</h1>")
                else:
                    return HttpResponse("<h1>Invalid User password</h1>")
                
        elif type == 'admin':
            admin = Admin.objects.get(email=email)
            if admin:
                
                if password == admin.password:
                    
                    return HttpResponse("<h1>Admin Log In successful</h1>")
                else:
                    return HttpResponse("<h1>Invalid Admin password</h1>")
    
    else:
        return render(request, 'loginapp/login.html')
        