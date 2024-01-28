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
        listOFItem = request.POST.get("listOFItem", False)
        data = json.loads(listOFItem)
        typoe="joma"
        print(data)
        for d in data:
            with connection.cursor() as cursor_1:
                cursor_1.execute("INSERT INTO dailysheet_table(date,item,amount,status,type) VALUES ('"+str(d["date"]) + "','"+str(d["item"]) + "','"+str(d["amount"]) + "','"+str(d["status"]) + "','"+str(typoe) + "')")
                connection.commit()
        
            with connection.cursor() as cursor_2:
                cursor_2.execute("select date, khatiyanName,joma, khoroch, balance from khatiyan_full where khatiyanName='" +str(d["item"]) + "' order by serial desc limit 1")
                row1 = cursor_2.fetchone()
            balance = row1[4]
            balance += int(d["amount"])
            khoroch = 0
            with connection.cursor() as cursor_3:
                cursor_3.execute("INSERT INTO khatiyan_full(date,khatiyanName,details,joma,khoroch,balance,type) VALUES ('"+str(d["date"]) + "','" +str(d["item"]) + "','" +str(d["details"]) + "','"+str(d["amount"]) + "','"+str(khoroch) + "','"+str(balance) + "','"+str(d["type"]) + "')")
                connection.commit()
         

    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def createDailysheetKhoroch(request):
    if request.method == 'POST':

        typoe="khoroch"
        listOFItem = request.POST.get("listOFItem", False)
        data = json.loads(listOFItem)
        for d in data:
            with connection.cursor() as cursor_1:
                cursor_1.execute("INSERT INTO dailysheet_table(date,item,amount,status,type) VALUES ('"+str(d["date"]) + "','" +str(d["item"]) + "','"+str(d["amount"]) + "','"+str(d["status"]) + "','"+str(typoe) + "')")
                connection.commit()
        
            with connection.cursor() as cursor_2:
                cursor_2.execute("select date, khatiyanName,joma, khoroch, balance from khatiyan_full where khatiyanName='" +str(d["item"]) + "' order by date desc limit 1")
                row1 = cursor_2.fetchone()
            balance = row1[4]
            balance -= int(d["amount"])
            joma = 0
            with connection.cursor() as cursor_3:
                cursor_3.execute("INSERT INTO khatiyan_full(date,khatiyanName,details,joma,khoroch,balance,type) VALUES ('"+str(d["date"]) + "','" +str(d["item"]) + "','" +str(d["details"]) + "','"+str(joma) + "','"+str(d["amount"]) + "','"+str(balance) + "','"+str(d["type"]) + "')")
                connection.commit()
        
        
        
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def dailysheetJomaKhorochList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, item from dailysheet_table group by date")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'item')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def getJomaDataList(request):
    if request.method == 'POST':
        date = request.POST.get("date", False)
        type="joma"
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select item, amount from dailysheet_table where date='"+str(date)+"' and type='"+str(type)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('item','amount')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
           
            return HttpResponse(json_data, content_type="application/json")
        
@csrf_exempt
def getKhorochDataList(request):
    if request.method == 'POST':
        date = request.POST.get("date", False)
        type="khoroch"
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select item, amount from dailysheet_table where date='"+str(date)+"' and type='"+str(type)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('item','amount')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")


