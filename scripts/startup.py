import os
from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = os.getenv('ADMIN_USERNAME', 'admin')
    email = os.getenv('ADMIN_EMAIL', 'calvincetom@outlook.com')
    password = os.getenv('ADMIN_PASSWORD', 'django')
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Created superuser '{username}'")
    else:
        print(f"Superuser '{username}' already exists")

if __name__ == '__main__':
    create_superuser()