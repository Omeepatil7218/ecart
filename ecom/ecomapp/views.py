from django.shortcuts import render,HttpResponse,redirect
from ecomapp import urls
from ecomapp import models 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, "Register.html")
    else:
        nm = request.POST['uname']
        p = request.POST['upass']
        cp = request.POST['ucpass']
        # print(un)
        # print(up)
        # print(ucp)
        context = {}
        if p != cp:
            context['error'] = "password does not match"
            return render(request,"Register.html",context)
        elif len(p) > 5:
            context['error'] = "password should have less then 6 characters"
            return render(request,"Register.html",context)
        else:
            try:
                u = User.objects.create(username = nm)
                u.set_password(p)
                u.save()
            
                context['success'] = "Successfully Registered !"
                return render(request,"Register.html",context)
            except:
                 context['error']='user already exists!!'
                 return render(request,"register.html", context)
def user_login(request):
    if request.method=='GET':
        
         return render(request, "login.html")
    
    else:
        nm= request.POST['uname']
        p= request.POST['upass']
        u  = authenticate(username=nm, password=p)
        if u  is not None:
            login(request,u)
            return render(request,"index.html")
        else:
            context={}
            context['error']='user or password isincorrect!!!'
            return render (request,"login.html",context)

def home(request):
    return render(request,"index.html")