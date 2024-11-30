from django.contrib import admin
from .models import Books,Categories

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display=["id","Book_name","Book_author","Book_Genres","Book_price","Book_descripition","Book_category"]

admin.site.register(Books,BooksAdmin)

class BooksCategories(admin.ModelAdmin):
    list_display=["id","category_name","category_slug"]

admin.site.register(Categories,BooksCategories)
