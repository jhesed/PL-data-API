from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import OperationalParametersModel
from .serializers import OperationalParametersSerializer


@api_view(["POST"])
@parser_classes([JSONParser])
def create_operational_parameter(request):
    data = request.data
    if isinstance(data, list):
        serializer = OperationalParametersSerializer(
            data=request.data, many=True
        )
    else:
        serializer = OperationalParametersSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def list_all_operational_parameters(request):
    queryset = OperationalParametersModel.objects.all()
    serializer = OperationalParametersSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def list_operational_parameters_by_plant(request):
    plant_id = request.query_params.get("plant_id")
    queryset = OperationalParametersModel.objects.filter(plant_id=plant_id)
    serializer = OperationalParametersSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_operational_parameter(request, pk):
    op_id = request.query_params.get("op_id")

    try:
        op = OperationalParametersModel.objects.get(pk=pk)
        serializer = OperationalParametersSerializer(op)
    except OperationalParametersModel.DoesNotExist:
        return Response(status=404)
    else:
        return Response(serializer.data)
