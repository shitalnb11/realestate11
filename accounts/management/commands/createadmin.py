from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a default superuser on deploy'

    def handle(self, *args, **options):
        username = "admin"
        email = "admin@gmail.com"
        password = "Admin@12345"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("✅ Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("ℹ️ Superuser already exists."))
