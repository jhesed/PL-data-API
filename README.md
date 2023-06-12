# PL-data-API

# Setup

## Setup local admin user

If using windows
```
.\.test_env.bat
cd .\pl_data_api\
python manage.py createsuperuser --username=admin --email=admin@example.com
```

If not using a TTY environment:
```
python manage.py shell  # Or via pycharm, but load .test_env

from django.contrib.auth import get_user_model
User = get_user_model()

# Replace with correct values
User.objects.create_superuser('admin', 'admin@example.com', 'password')  
```


# Admin URL
http://localhost:8000/admin

# Migrations
```commandline
# Or if via pycharm, load .test_env
python manage.py makemigrations
python manage.py migrate
```