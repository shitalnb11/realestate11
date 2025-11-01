from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a UserProfile for each new user."""
    if created:
        UserProfile.objects.create(
            user=instance,
            full_name=instance.username,
            phone="",
            role="buyer"  # default role; can change later in admin
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Ensure the profile is saved when the user is updated."""
    # Only save if the user already has a profile (avoids crash)
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
