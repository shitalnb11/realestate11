from django.apps import AppConfig
import os
from django.db.models.signals import post_migrate

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # ✅ Signal connect after migrations are done
        post_migrate.connect(create_superuser, sender=self)


def create_superuser(sender, **kwargs):
    import os
    from django.contrib.auth import get_user_model
    User = get_user_model()

    if os.environ.get('CREATE_SUPERUSER_ON_DEPLOY') == '1':
        username = "admin"
        email = "admin@gmail.com"
        password = "Admin@12345"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print("✅ Superuser created successfully after migrate!")
        else:
            print("ℹ️ Superuser already exists.")
