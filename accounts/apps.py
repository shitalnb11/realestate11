from django.apps import AppConfig
import os  # ✅ added

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # ✅ This runs only after all Django apps are ready
        if os.environ.get('CREATE_SUPERUSER_ON_DEPLOY') == '1':
            try:
                from django.contrib.auth import get_user_model
                User = get_user_model()  # ✅ safer than direct import
                username = "admin"
                email = "admin@gmail.com"
                password = "Admin@12345"
                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(username=username, email=email, password=password)
                    print("✅ Superuser created automatically on deploy!")
            except Exception as e:
                print(f"⚠️ Error creating superuser: {e}")
