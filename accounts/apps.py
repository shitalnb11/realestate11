from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # ✅ Import signals (for UserProfile auto-create)
        import accounts.signals

        # ✅ Connect post_migrate signal safely (auto superuser)
        from django.contrib.auth import get_user_model
        from django.conf import settings
        from django.db.utils import OperationalError

        def create_superuser(sender, **kwargs):
            import os
            User = get_user_model()
            try:
                if os.environ.get('CREATE_SUPERUSER_ON_DEPLOY') == '1':
                    username = "admin"
                    email = "admin@gmail.com"
                    password = "Admin@12345"

                    if not User.objects.filter(username=username).exists():
                        User.objects.create_superuser(username=username, email=email, password=password)
                        print("✅ Superuser created successfully after migrate!")
                    else:
                        print("ℹ️ Superuser already exists.")
            except OperationalError:
                # Database may not be ready on first migrate
                print("⚠️ Skipping superuser creation — database not ready yet.")

        post_migrate.connect(create_superuser, sender=self)
