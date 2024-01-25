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
  
    Joma = 0
    Khoroch = 0
    balance = 0
    if request.method == 'POST':
       
        khatiyanName = request.POST.get("khatiyanName", False)
        date = request.POST.get("date", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO khatiyan_full(date,khatiyanName,joma,khoroch, balance) VALUES ('"+str(
                date) + "','"+str(khatiyanName) + "','"+str(Joma) + "','"+str(Khoroch) + "','"+str(balance) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def getKhatiyanList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, khatiyanName from khatiyan_full group by khatiyanName")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'khatiyanName')
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
                "select date, joma, khoroch, balacne from khatiyan_full WHERE khatiyanName='"+str(khatiyanName)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'joma', 'khoroch', 'balance')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)

            return HttpResponse(json_data, content_type="application/json")
