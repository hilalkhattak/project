from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.productPage, name='product'),
    path('contact/', views.home, name='contact'),
    path('repair/', views.about, name='repair'),

]
