# PL-data-API

# Setup

# Migrations
```commandline
# Or if via pycharm, load .test_env
python manage.py makemigrations
python manage.py migrate
```

## Setup local admin user

If using windows
```
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


## Tests

1. Pre-populate plant model first with some value so APIs won't return bad requests

# Run
```commandline
.\.test_env.bat
cd .\pl_data_api\
python manage.py runserver
```

## Django and windows env variable
To set up environment variables for database-related configurations such as `DB_NAME`, `DB_HOST`, etc., you can follow these steps:

1. Open the Start menu and search for "Environment Variables".
2. Click on "Edit the system environment variables" to open the System Properties dialog box.
3. In the System Properties dialog, click on the "Environment Variables" button.
4. Under "User variables" or "System variables", click on the "New" button to create a new environment variable.
5. Enter the name of the variable in the "Variable name" field, such as `DB_NAME`.
6. Enter the value of the variable in the "Variable value" field, such as the name of your database.
7. Repeat steps 4-6 for other database-related environment variables like `DB_HOST`, `DB_USER`, `DB_PASSWORD`, etc.
8. Click "OK" to save the new environment variables.

After setting up the environment variables, you can access them in your Django application's settings file (`settings.py`). Here's an example of how you can use these environment variables in Django:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

In the example above, the `os.environ.get()` function is used to retrieve the values of the environment variables. These values are then used to populate the corresponding database configuration settings in the Django `DATABASES` dictionary.

Remember to restart your Django application or command prompt for the changes to take effect.