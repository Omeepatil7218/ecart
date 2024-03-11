from django.urls import path
from ecomapp import views

urlpatterns = [
path('register',views.register),
path('login',views.user_login),
path('home',views.home),
]
