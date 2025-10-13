from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib.auth.models import User
        if os.environ.get('CREATE_SUPERUSER_ON_DEPLOY') == '1':
            username = "admin"
            email = "admin@gmail.com"
            password = "Admin@12345"
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                print("✅ Superuser created automatically on deploy!")