from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def user_login(request):
    if request.method=="GET":
        return render(request,"login.html")
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("/login")
        else:
            return render(request,"login.html",{"message":"Login failed"})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

def register(request):
    if request.method=="GET":
        # form=UserCreationForm()
        form=CustomUserCreationForm()
        return render(request,"register.html",{"form":form})
    else:
        # form=UserCreationForm(request.POST)
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/about")
        return render(request,"register.html",{"form":form})
