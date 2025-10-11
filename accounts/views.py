from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, ContactMessage, Property
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

        # ✅ Validation
        if not full_name or not email or not phone or not password1 or not password2:
            messages.error(request, "⚠️ All fields are required.")
            return render(request, "registration/register.html")

        if password1 != password2:
            messages.error(request, "⚠️ Passwords do not match.")
            return render(request, "registration/register.html")

        if User.objects.filter(username=email).exists():
            messages.error(request, "⚠️ This email is already registered. Please login.")
            return render(request, "registration/register.html")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password1
        )

        UserProfile.objects.create(
            user=user,
            full_name=full_name,
            phone=phone
        )

        messages.success(request, "✅ Registration successful! Please login.")
        return redirect("login")

    return render(request, "registration/register.html")


# -----------------------------
# LOGIN VIEW
# -----------------------------
def user_login(request):
    # 🧹 Always clear old messages first (GET or POST)
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # consume old messages

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("properties")  # ✅ Successful login — direct redirect
        else:
            # ❌ Invalid credentials — show error message only once
            messages.error(request, "⚠️ Invalid username or password!")
            return render(request, "registration/login.html")  # ✅ No redirect

    return render(request, "registration/login.html")



# -----------------------------
# PROPERTIES PAGE (shows all properties)
# -----------------------------
@login_required(login_url="login")
def properties(request):
    all_properties = Property.objects.all()  # ✅ Fetch all Property records
    return render(request, "properties.html", {"properties": all_properties})


# -----------------------------
# ADD PROPERTY VIEW
# -----------------------------
@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user  # if model has owner field
            property.save()
            messages.success(request, "✅ Property added successfully!")
            return redirect('properties')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


# -----------------------------
# OTHER VIEWS
# -----------------------------
def home(request):
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "✅ Message sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")


# -----------------------------
# PROPERTY DETAIL VIEW (for single property)
# -----------------------------
def property_detail(request, property_id=None):
    if property_id:
        try:
            property_obj = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            messages.error(request, "❌ Property not found.")
            return redirect("properties")
    else:
        property_obj = None

    return render(request, "property.html", {"property": property_obj})
