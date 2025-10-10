from django.contrib import admin
from .models import UserProfile, ContactMessage, Property


# ✅ Register UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'user')


# ✅ Register ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Use only fields that actually exist in your model
    list_display = ('name', 'email', 'message')  # Remove phone, created_at if not in model


# ✅ Register Property
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'property_type')
