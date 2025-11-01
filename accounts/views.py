from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from functools import wraps
from django.db.models import Avg
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from .models import (
    UserProfile,
    ContactMessage,
    Property,
    Rating,
    Report
)
from .forms import PropertyForm, RatingForm


# --------------------------------------------------
# HELPER DECORATOR: Restrict view to sellers only
# --------------------------------------------------
def seller_required(view_func):
    """
    Restrict access to sellers only.
    Redirect others (buyers/admins) with an error message.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "⚠️ Please log in first.")
            return redirect('login')

        profile = getattr(request.user, 'userprofile', None)
        if not profile or profile.role != 'seller':
            messages.error(request, "⚠️ Only sellers can add or manage properties.")
            return redirect('home')

        return view_func(request, *args, **kwargs)
    return wrapper


# --------------------------------------------------
# CLEAR MESSAGES HELPER
# --------------------------------------------------
def clear_messages(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass


# --------------------------------------------------
# REGISTER VIEW
# --------------------------------------------------
def register(request):
    if request.method == "POST":
        clear_messages(request)

        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        role = request.POST.get("role", "buyer")

        if not all([full_name, email, phone, password1, password2]):
            messages.error(request, "⚠️ All fields are required.")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "⚠️ Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "⚠️ This email is already registered. Please login.")
            return redirect("login")

        user = User.objects.create_user(username=email, email=email, password=password1)
        profile = user.userprofile
        profile.full_name = full_name
        profile.phone = phone
        profile.role = role
        profile.save()

        messages.success(request, "✅ Registration successful! Please login.")
        return redirect("login")

    clear_messages(request)
    return render(request, "registration/register.html")


# --------------------------------------------------
# LOGIN VIEW
# --------------------------------------------------
@never_cache
def user_login(request):
    clear_messages(request)

    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={'full_name': user.username, 'phone': '', 'role': 'admin' if user.is_superuser else 'buyer'}
            )

            if profile.role == 'seller':
                messages.success(request, f"✅ Welcome Seller, {user.username}!")
                return redirect('add_property')
            elif profile.role == 'admin':
                messages.success(request, f"✅ Welcome Admin, {user.username}!")
                return redirect('admin_dashboard')
            else:
                messages.success(request, f"✅ Welcome Buyer, {user.username}!")
                return redirect('properties')
        else:
            messages.error(request, "⚠️ Invalid email or password!")
            return render(request, "registration/login.html")

    return render(request, "registration/login.html")


# --------------------------------------------------
# LOGOUT VIEW — Clears session, cache, and autofill
# --------------------------------------------------
def user_logout(request):
    """
    Logs out user, clears session and browser cache,
    and resets login form fields on next load.
    """
    logout(request)
    request.session.flush()
    list(messages.get_messages(request))
    messages.success(request, "✅ You have been logged out successfully!")

    response = redirect('login')

    # 🚫 Disable caching completely
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    # 🧹 Add temp cookie to clear login fields
    response.set_cookie('clear_login', '1', max_age=2)

    return response


# --------------------------------------------------
# HOME VIEW
# --------------------------------------------------
def home(request):
    return render(request, "index.html")


# --------------------------------------------------
# CONTACT VIEW
# --------------------------------------------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, "✅ Message sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")


# --------------------------------------------------
# PROPERTIES VIEW
# --------------------------------------------------
@login_required(login_url="login")
def properties(request):
    profile = getattr(request.user, 'userprofile', None)
    if profile and profile.role == 'seller':
        all_properties = Property.objects.filter(seller=request.user)
    else:
        all_properties = Property.objects.all()

    for prop in all_properties:
        prop.avg_rating = Rating.objects.filter(property=prop).aggregate(Avg('rating'))['rating__avg'] or 0

    return render(request, "properties.html", {"properties": all_properties})


# --------------------------------------------------
# ADD PROPERTY VIEW
# --------------------------------------------------
@login_required(login_url="login")
@seller_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user
            property.save()
            messages.success(request, "✅ Property added successfully!")
            return redirect('properties')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = PropertyForm()

    return render(request, 'add_property.html', {'form': form})


# --------------------------------------------------
# PROPERTY DETAIL VIEW
# --------------------------------------------------
@login_required
def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)

    # Related images and videos
    images = property_obj.images.all()
    videos = getattr(property_obj, 'videos', None)

    # Ratings
    ratings = Rating.objects.filter(property=property_obj).order_by('-created_at')
    average_rating = ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    rating_percentage = (average_rating / 5) * 100 if average_rating else 0

    # Similar properties (same city/type)
    similar_properties = Property.objects.filter(
        city=property_obj.city,
        property_type=property_obj.property_type
    ).exclude(pk=property_obj.pk)[:3]

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.property = property_obj
            rating.user = request.user
            rating.save()
            messages.success(request, "✅ Your rating has been submitted!")
            return redirect('property_detail', pk=property_obj.pk)
    else:
        form = RatingForm()

    context = {
        'property': property_obj,
        'images': images,
        'videos': videos,
        'form': form,
        'ratings': ratings,
        'average_rating': average_rating,
        'rating_percentage': rating_percentage,
        'similar_properties': similar_properties,
    }

    return render(request, 'property_detail.html', context)
# --------------------------------------------------
# ADMIN DASHBOARD VIEW
# --------------------------------------------------
@login_required(login_url="login")
def admin_dashboard(request):
    total_properties = Property.objects.count()
    approved_properties = Property.objects.filter(is_approved=True).count()
    reported_properties = Property.objects.filter(is_reported=True).count()
    pending_properties = total_properties - (approved_properties + reported_properties)
    total_users = User.objects.count()
    total_messages = ContactMessage.objects.count()

    context = {
        "total_properties": total_properties,
        "approved_properties": approved_properties,
        "reported_properties": reported_properties,
        "pending_properties": pending_properties,
        "total_users": total_users,
        "total_messages": total_messages,
        "year": datetime.now().year
    }
    return render(request, "admin_dashboard.html", context)


# --------------------------------------------------
# USER PROFILE VIEW
# --------------------------------------------------
@login_required(login_url="login")
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'full_name': request.user.username, 'phone': '', 'role': 'admin' if request.user.is_superuser else 'buyer'}
    )
    return render(request, 'profile.html', {'profile': user_profile})


# --------------------------------------------------
# PROPERTY MAP VIEW
# --------------------------------------------------
def property_map(request):
    properties = Property.objects.filter(is_approved=True)
    return render(request, 'property_map.html', {'properties': properties})

 
 

def property_redirect(request):
    return redirect('properties')


