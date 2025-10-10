from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    # ✅ Admin
    path('admin/', admin.site.urls),

    # ✅ Home Page
    path('', views.home, name='home'),

    # ✅ Contact Page
    path('contact/', views.contact, name='contact'),

    # ✅ Properties Page (🔥 FIXED)
    path('properties/', views.properties, name='properties'),
    path('add-property/', views.add_property, name='add_property'),

    path('property/', views.property, name='property'),

    # ✅ Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # ✅ Register Page
    path('register/', views.register, name='register'),

    # ✅ Forgot / Reset Password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
   

]
