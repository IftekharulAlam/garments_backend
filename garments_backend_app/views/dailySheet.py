# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse
from datetime import date
@csrf_exempt
def createDailysheetJoma(request):
    if request.method == 'POST':
        datetime = request.POST.get("datetime", False)
        listOFItem = request.POST.get("listOFItem", False)
        listOFAmount = request.POST.get("listOFAmount", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO dailysheetjoma_table(date,item,amount) VALUES ('"+str(
                datetime) + "','"+str(listOFItem) + "','"+str(listOFAmount) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def createDailysheetKhoroch(request):
    if request.method == 'POST':
        datetime = request.POST.get("datetime", False)
        listOFItem = request.POST.get("listOFItem", False)
        listOFAmount = request.POST.get("listOFAmount", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO dailysheetkhoroch_table(date,item,amount) VALUES ('"+str(
                datetime) + "','"+str(listOFItem) + "','"+str(listOFAmount) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def dailysheetJomaKhorochList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, item from dailysheetkhoroch_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'item')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")