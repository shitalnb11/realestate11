from django.contrib import admin
from .models import UserProfile, ContactMessage, Property, Report


# ✅ User Profiles
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'user')


# ✅ Contact Messages
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  # you have these fields
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


# ✅ Property Listings
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'property_type', 'is_approved', 'is_reported', 'created_at')
    list_filter = ('is_approved', 'is_reported', 'property_type')
    search_fields = ('title', 'location')
    ordering = ('-created_at',)

    # ✅ Add quick admin actions
    actions = ['approve_properties', 'reject_properties', 'mark_reported']

    def approve_properties(self, request, queryset):
        queryset.update(is_approved=True)
    approve_properties.short_description = "✅ Approve selected properties"

    def reject_properties(self, request, queryset):
        queryset.update(is_approved=False)
    reject_properties.short_description = "❌ Reject selected properties"

    def mark_reported(self, request, queryset):
        queryset.update(is_reported=True)
    mark_reported.short_description = "⚠️ Mark selected as reported"


# ✅ Reported Properties
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('property', 'reported_by', 'reason', 'resolved', 'created_at')
    list_filter = ('resolved', 'created_at')
    search_fields = ('property__title', 'reported_by__username', 'reason')

    # Optional quick action
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True)
    mark_resolved.short_description = "✅ Mark selected reports as resolved"
