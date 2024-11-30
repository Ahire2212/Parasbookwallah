from django.shortcuts import render
from .models import Books,Categories
from django.views.generic import ListView

# Create your views here.

def kids_Books(request):
    items=Books.cust_manager.kids_Books()
    return render(request,"Books/kids_books.html",{"kids_Books":items})

def Childrens_Books(request):
    items=Books.cust_manager.Childrens_Books()
    return render(request,"Books/Childrens_Books.html",{"Childrens_Books":items})

def Comics(request):
    items=Books.cust_manager.Comics()
    return render(request,"Books/Comics.html",{"Comics":items})

def Manga_Comics(request):
    items=Books.cust_manager.Manga_Comics()
    return render(request,"Books/Manga_Comics.html",{"Manga_Comics":items})

def Coffee_Table_Books(request):
    items=Books.cust_manager.Coffee_Table_Books()
    return render(request,"Books/Coffee_Table_Books.html",{"Coffee_Table_Books":items})

def Box_set_Books(request):
    items=Books.cust_manager.Box_set_Books()
    return render(request,"Books/Box_set_Books.html",{"Box_set_Books":items})

