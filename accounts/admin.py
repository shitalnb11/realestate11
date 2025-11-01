from django.contrib import admin
from django import forms
from .models import (
    UserProfile,
    ContactMessage,
    Property,
    PropertyImage,
    PropertyVideo,
    Report
)

# =========================================================
# USER PROFILES
# =========================================================
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'user', 'role')
    search_fields = ('full_name', 'phone', 'user__username')
    list_filter = ('role',)


# =========================================================
# CONTACT MESSAGES
# =========================================================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


# =========================================================
# INLINE FORMS (Fix for Cloudinary Uploads)
# =========================================================
class PropertyImageInlineForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enctype = "multipart/form-data"  # Ensures files are processed


class PropertyVideoInlineForm(forms.ModelForm):
    class Meta:
        model = PropertyVideo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enctype = "multipart/form-data"


# =========================================================
# PROPERTY IMAGES INLINE
# =========================================================
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    form = PropertyImageInlineForm
    extra = 1
    verbose_name = "Property Image"
    verbose_name_plural = "Property Images"

    # Optional: show preview in admin
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="80" style="object-fit:cover; border-radius:4px;"/>'
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"


# =========================================================
# PROPERTY VIDEOS INLINE
# =========================================================
class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    form = PropertyVideoInlineForm
    extra = 1
    verbose_name = "Property Video"
    verbose_name_plural = "Property Videos"

    readonly_fields = ['video_preview']

    def video_preview(self, obj):
        if obj.video:
            return f'<video width="150" controls><source src="{obj.video.url}" type="video/mp4">Your browser does not support video playback.</video>'
        return "-"
    video_preview.allow_tags = True
    video_preview.short_description = "Preview"


# =========================================================
# PROPERTY ADMIN
# =========================================================
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'seller', 'location', 'city', 'price',
        'property_type', 'status', 'is_approved', 'is_reported', 'created_at'
    )
    list_filter = ('is_approved', 'is_reported', 'property_type', 'status', 'city')
    search_fields = ('title', 'location', 'city', 'seller__username')
    ordering = ('-created_at',)
    inlines = [PropertyImageInline, PropertyVideoInline]

    # ✅ Quick admin actions
    actions = ['approve_properties', 'reject_properties', 'mark_reported']

    def approve_properties(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "✅ Selected properties have been approved.")
    approve_properties.short_description = "Approve selected properties"

    def reject_properties(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, "❌ Selected properties have been rejected.")
    reject_properties.short_description = "Reject selected properties"

    def mark_reported(self, request, queryset):
        queryset.update(is_reported=True)
        self.message_user(request, "⚠️ Selected properties marked as reported.")
    mark_reported.short_description = "Mark selected as reported"


# =========================================================
# REPORT ADMIN
# =========================================================
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('property', 'reported_by', 'reason', 'resolved', 'created_at')
    list_filter = ('resolved', 'created_at')
    search_fields = ('property__title', 'reported_by__username', 'reason')
    ordering = ('-created_at',)

    # ✅ Quick action to mark as resolved
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True)
        self.message_user(request, "✅ Selected reports have been marked as resolved.")
    mark_resolved.short_description = "Mark selected reports as resolved"
