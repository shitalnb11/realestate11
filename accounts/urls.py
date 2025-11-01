from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('properties/', views.properties, name='properties'),
    path('property/', views.property_redirect, name='property_redirect'),  # 👈 ADD THIS LINE
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('add-property/', views.add_property, name='add_property'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    

]
