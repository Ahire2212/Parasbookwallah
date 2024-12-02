from django.urls import path,include
from .import views
from cart import urls
from django.conf.urls.static import static


urlpatterns =[
    
path('kids_Books/',views.kids_Books,name="kids_Books"),
path('Childrens_Books/',views.Childrens_Books,name="Childrens_Books"),
path('Box_set_Books/',views.Box_set_Books,name="Box_set_Books"),
path('Comics/',views.Comics,name="Comics"),
path('Manga_Comics/',views.Manga_Comics,name="Manga_Comics"),
path('Coffee_Table_Books/',views.Coffee_Table_Books,name="Coffee_Table_Books"),
path('cart/',include('cart.urls')),
path('search/',views.search,name="search")
# path('burgers/',views.burger,name="burgerpage"),
# path('beverages-desserts/',views.soft_drinks,name="softdrinkpage"),
# path('rice-bowlz/',views.rice_bowl,name="rbpage")

]