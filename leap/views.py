from re import A, I
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import *


@api_view(["GET"])
def leap_api(request, year):
    valid = get_leap_year(int(year))
    return Response({year: valid}, status=status.HTTP_200_OK)


@api_view(["POST"])
def range_leap_year_api(request):
    data = request.data
    start = None
    end = None
    res = {}
    if "start" in data.keys():
        start = int(data["start"])
    elif "end" in data.keys():
        end = int(data["end"])
    if start and end is not None:
        res["leap_year_list"] = get_range_leap_year(start, end)

    return Response(dict(list_leap=res))
