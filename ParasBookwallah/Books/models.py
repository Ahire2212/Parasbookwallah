from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class custom_manager (models.Manager):

    def kids_Books(self):
        return super().get_queryset().filter(Book_category_id=1)

    def Childrens_Books(self):
        return super().get_queryset().filter(Book_category_id=2)

    def Comics(self):
        return super().get_queryset().filter(Book_category_id=3)

    def Manga_Comics(self):
        return super().get_queryset().filter(Book_category_id=4)

    def Classic_Books(self):
        return super().get_queryset().filter(Book_category_id=5)

    def Non_Fic_Books(self):
        return super().get_queryset().filter(Book_category_id=6)

    def Fic_Books(self):
        return super().get_queryset().filter(Book_category_id=7)

    def Romances_Books(self):
        return super().get_queryset().filter(Book_category_id=8)

    def Vintage_Books(self):
        return super().get_queryset().filter(Book_category_id=9)

    def Coffee_Table_Books(self):
        return super().get_queryset().filter(Book_category_id=10)
    
    def Box_set_Books(self):
        return super().get_queryset().filter(Book_category_id=11)
    

class Categories(models.Model):
    def __str__(self):
        return self.category_name

    category_name=models.CharField(max_length=100,null=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)


class Books(models.Model):
    Book_name=models.CharField(max_length=100,null=False,default="")
    Book_author=models.CharField(max_length=50,null=False,default="")
    Book_price=models.PositiveIntegerField(default=0)
    Book_Genres=models.CharField(max_length=50,null=False,default="")
    Book_descripition=models.TextField(default="Book descripition")
    Book_image=models.ImageField(upload_to="products/",default="")
    Book_category=models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    cust_manager=custom_manager()