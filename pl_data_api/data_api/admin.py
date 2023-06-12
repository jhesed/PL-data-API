from django.contrib import admin

from .models import PlantModel, OperationalParametersModel

# Register your models here.

admin.site.register(PlantModel)
admin.site.register(OperationalParametersModel)
