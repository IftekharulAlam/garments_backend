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
    Balance = 0
    if request.method == 'POST':
        khatiyanName = request.POST.get("khatiyanName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO khatiyan_table(Date,khatiyanName,Joma,Khoroch,Balance) VALUES ('"+str(
                Date) + "','"+str(khatiyanName) + "','"+str(Joma) + "','"+str(Khoroch) + "','"+str(Balance) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")



@csrf_exempt
def getKhatiyanList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select Date, khatiyanName, Joma, Khoroch, Balance from khatiyan_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('Date', 'khatiyanName',
                    'Joma', 'Khoroch', 'Balance')
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
                "select Date, Joma, Khoroch, Balance from khatiyan_table WHERE khatiyanName='"+str(khatiyanName)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('Date', 'Joma', 'Khoroch', 'Balance')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)

            return HttpResponse(json_data, content_type="application/json")


