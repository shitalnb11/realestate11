from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# =========================================================
# USER PROFILE MODEL
# =========================================================
USER_ROLES = [
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
    ('admin', 'Admin'),
]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='buyer')
    profile_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"


# =========================================================
# CONTACT MESSAGE MODEL
# =========================================================
class ContactMessage(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


# =========================================================
# PROPERTY CONSTANTS
# =========================================================
PROPERTY_TYPES = [
   ('apartment', 'Apartment'),
    ('villa', 'Villa'),
    ('house', 'House'),
    ('rowhouse', 'Row House'),
    ('land', 'Land'),
    ('commercial', 'Commercial'),

    # ✅ Newly added BHK options
    ('1bhk', '1 BHK'),
    ('2bhk', '2 BHK'),
    ('3bhk', '3 BHK'),
    ('4bhk', '4 BHK'),
]

PROPERTY_STATUS = [
    ('sale', 'For Sale'),
    ('rent', 'For Rent'),
]

FURNISHING_TYPES = [
    ('furnished', 'Furnished'),
    ('semi_furnished', 'Semi-Furnished'),
    ('unfurnished', 'Unfurnished'),
]


# =========================================================
# PROPERTY MODEL
# =========================================================
class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=20, choices=PROPERTY_STATUS, default='sale')
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    furnishing = models.CharField(max_length=50, choices=FURNISHING_TYPES, blank=True, null=True)
    area_sqft = models.FloatField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)  # main thumbnail
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ Add these two new fields
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title



# =========================================================
# PROPERTY IMAGES (Multiple Images per Property)
# =========================================================
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.property.title}"


# =========================================================
# PROPERTY VIDEOS (Optional Video Upload)
# =========================================================
class PropertyVideo(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='videos')
    video = CloudinaryField('video')

    def __str__(self):
        return f"Video for {self.property.title}"


# =========================================================
# REPORT MODEL
# =========================================================
class Report(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report on {self.property.title} by {self.reported_by.username}"
class Rating(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.property.title} - {self.rating}/5"
