from django.urls import path
from .views import (
    create_operational_parameter,
    list_all_operational_parameters,
    list_operational_parameters_by_plant,
    get_operational_parameter,
)

urlpatterns = [
    path(
        "op/create/",
        create_operational_parameter,
        name="create-operational-parameter",
    ),
    path(
        "op/",
        list_all_operational_parameters,
        name="list-operational-parameter",
    ),
    path(
        "op/<int:pk>/",
        get_operational_parameter,
        name="get_operational_parameter",
    ),
    path(
        "op/list/by-plant/",
        list_operational_parameters_by_plant,
        name="list_operational_parameters_by_plant",
    ),
]
