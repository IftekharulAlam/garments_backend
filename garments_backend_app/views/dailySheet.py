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
                cursor_1.execute("INSERT INTO dailysheet_table(date,item,details,amount,status,type) VALUES ('"+str(d["date"]) + "','"+str(d["item"]) + "','"+str(d["details"]) + "','"+str(d["amount"]) + "','"+str(d["status"]) + "','"+str(typoe) + "')")
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
                cursor_1.execute("INSERT INTO dailysheet_table(date,item,details,amount,status,type) VALUES ('"+str(d["date"]) + "','" +str(d["item"]) + "','"+str(d["details"]) + "','"+str(d["amount"]) + "','"+str(d["status"]) + "','"+str(typoe) + "')")
                connection.commit()
        
            with connection.cursor() as cursor_2:
                cursor_2.execute("select date, khatiyanName,joma, khoroch, balance from khatiyan_full where khatiyanName='" +str(d["item"]) + "' order by serial desc limit 1")
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
                "select date, status from dailysheet_table group by date")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'status')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def getJomaDataList(request):
    if request.method == 'POST':
        date = request.POST.get("date", False)
        type="joma"
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select item, amount, date, status, type from dailysheet_table where date='"+str(date)+"' and type='"+str(type)+"'")
            row1 = cursor_1.fetchall()
        with connection.cursor() as cursor_2:
            cursor_2.execute(
                "select item, amount, date, status, type from dailysheet_table where date='"+str(date)+"' and type='"+str("khoroch")+"' and item='"+str("DailySheet")+"'")
            row2 = cursor_2.fetchone()
            
            if row2 == None:
                pass
                # mytuple1 = ("khoroch",0,0,0,"pending")
                # list3 = list(row2)
                # list3[0] ="Khoroch" 
                # row2 = tuple(list3)
            
                # totalJoma=0
                # for row in row1:
                #     if row[0] == "DailySheet":
                #         totalJoma = row[1]
                # totalKhoroch = row2[1]
                # totalAmount = totalJoma - totalKhoroch
                # mytuple = ("Balance",totalAmount,row2[2],row2[3],row2[4])
                # row3 = row1
                # list1 = list(row3)
                # list1.append(row2)
                # list1.append(mytuple)
            
                # resulttuple = tuple(list1)
            else:
                list3 = list(row2)
                list3[0] ="Khoroch" 
                row2 = tuple(list3)
            
                totalJoma=0
                for row in row1:
                    if row[0] == "DailySheet":
                        totalJoma = row[1]
                totalKhoroch = row2[1]
                totalAmount = totalJoma - totalKhoroch
                mytuple = ("Balance",totalAmount,row2[2],row2[3],row2[4])
                row3 = row1
                list1 = list(row3)
                list1.append(row2)
                list1.append(mytuple)
           
                resulttuple = tuple(list1)
            
            list3 = list(row2)
            list3[0] ="Khoroch" 
            row2 = tuple(list3)
         
            totalJoma=0
            for row in row1:
                if row[0] == "DailySheet":
                    totalJoma = row[1]
            totalKhoroch = row2[1]
            totalAmount = totalJoma - totalKhoroch
            mytuple = ("Balance",totalAmount,row2[2],row2[3],row2[4])
            row3 = row1
            list1 = list(row3)
            list1.append(row2)
            list1.append(mytuple)
           
            resulttuple = tuple(list1)

            result = []

            keys = ('item','amount', 'date', 'status', 'type')
            for row in resulttuple:
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
                "select item, amount, date, status, type from dailysheet_table where date='"+str(date)+"' and type='"+str(type)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('item','amount', 'date', 'status', 'type')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")
        
@csrf_exempt
def getKhorochDataListForUpdate(request):
    if request.method == 'POST':
        date = request.POST.get("date", False)
        type = request.POST.get("type", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select item, amount, date, details, status, type from dailysheet_table where date='"+str(date)+"' and type='"+str(type)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('item','amount', 'date','details', 'status', 'type')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
          
            return HttpResponse(json_data, content_type="application/json")


