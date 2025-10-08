from django.contrib import admin
from .models import UserProfile, ContactMessage

# ✅ Register UserProfile (only once)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'user')

# ✅ Register ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
