from core.views import home
from django.urls import path
from core.views import *

urlpatterns = [
    path("", home, name="home"),
  
    path("shopping cart/", shop_cart, name="shopping_cart"),
    path("contact/", contact_view, name="contact"),
    path("blog/", blog, name="blog"),
    path("about us/", about_us, name="about_us"),
    path("checkout/", check, name="checkout"),
    path("blog details/", blog_details, name="blog_details"),
    path("shop/",shop, name="shop"),
    path("male fashion/",male_fashion, name="male_fashion"),
    path("shop/<slug:slug>/", shop_detail, name="shop_detail"),
    path('search/', search, name="search"),
]
