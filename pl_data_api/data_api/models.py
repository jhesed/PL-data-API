# Create your models here.
from django.db import models


class PlantModel(models.Model):

    # Keys
    plant_id = models.AutoField(primary_key=True)

    # Fields
    plant_name = models.CharField(max_length=100, null=True)

    # Meta Fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.plant_id}] {self.plant_name}"


class OperationalParametersModel(models.Model):

    # Keys
    op_id = models.AutoField(primary_key=True)
    plant_id = models.ForeignKey(
        PlantModel, on_delete=models.CASCADE, null=True
    )

    # Fields
    pressure = models.FloatField(null=True)
    flow = models.FloatField(null=True)
    level = models.FloatField(null=True)
    power = models.FloatField(null=True)
    scada_datetime = models.DateTimeField(null=True)

    # Meta Fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
