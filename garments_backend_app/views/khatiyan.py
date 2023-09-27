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
def createKhatiyan(request):
    Date = str(date.today())
    Joma = 0
    Khoroch = 0
    if request.method == 'POST':
        khatiyanName = request.POST.get("khatiyanName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO dailysheet_total(date,khatiyanName,totalJoma,totalKhoroch) VALUES ('"+str(
                Date) + "','"+str(khatiyanName) + "','"+str(Joma) + "','"+str(Khoroch) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def getKhatiyanList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, khatiyanName, totalJoma, totalKhoroch from dailysheet_total")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'khatiyanName', 'totalJoma', 'totalKhoroch')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getKhatiyanDetails(request):
    if request.method == 'POST':
        khatiyanName = request.POST.get("khatiyanName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, totalJoma, totalKhoroch from dailysheet_total WHERE khatiyanName='"+str(khatiyanName)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'totalJoma', 'totalKhoroch')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)

            return HttpResponse(json_data, content_type="application/json")
