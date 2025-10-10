from django.db import models
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return f"{self.name} - {self.email}"


 
 
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
 
    def __str__(self):
        return f"{self.name} - {self.email}"
 
 
PROPERTY_TYPES = [
    ('Apartment'),
    ('Villa'),
    ('House'),
    ('Land'),
    ('Commercial'),
]
 
 
class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # <-- automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)      # <-- automatically updated on save
 
 
    def __str__(self):
        return self.title