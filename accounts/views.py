from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, ContactMessage
from django.contrib.auth import login
from .models import Property
from .forms import PropertyForm
from django.http import HttpResponse 


# -----------------------------
# REGISTER VIEW
# -----------------------------
def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # ✅ Validation: all fields required
        if not full_name or not email or not phone or not password1 or not password2:
            messages.error(request, "⚠️ All fields are required.")
            return render(request, "registration/register.html")

        # ✅ Validation: password match
        if password1 != password2:
            messages.error(request, "⚠️ Passwords do not match.")
            return render(request, "registration/register.html")

        # ✅ Validation: check if email already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "⚠️ This email is already registered. Please login.")
            return render(request, "registration/register.html")

        # ✅ Create User
        user = User.objects.create_user(
            username=email,       # Using email as username
            email=email,
            password=password1
        )

        # ✅ Save Extra Details
        UserProfile.objects.create(
            user=user,
            full_name=full_name,
            phone=phone
        )

        # ✅ Success message
        messages.success(request, "✅ Registration successful! Please login.")
        return redirect("login")

    return render(request, "registration/register.html")


# -----------------------------
# LOGIN VIEW
# -----------------------------
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"🎉 Welcome {user.username}!")
            return redirect("properties")
        else:
            messages.error(request, "⚠️ Invalid username or password!")

    return render(request, "registration/login.html")

    
    storage = messages.get_messages(request)
    storage.used = True

    return render(request, "registration/login.html")

# -----------------------------
# PROPERTIES PAGE (LOGIN REQUIRED)
# -----------------------------
@login_required(login_url="login")
def properties(request):
    return render(request, "properties.html")


# -----------------------------
# OTHER VIEWS
# -----------------------------
def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "index.html")


def property(request):
    return render(request, "property.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # ✅ Save contact
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "✅ Message sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")



@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user  # if your model has owner field
            property.save()
            return redirect('properties')  # redirect to property listing page
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})
