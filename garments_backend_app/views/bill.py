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
def createBill(request):
    if request.method == 'POST':
        listOFItem = request.POST.get("bill", False)
        data = json.loads(listOFItem)
        partyName = data["shopName"]
        totalAmount = data["totalAmount"]
        date = data["date"]
     
        for d in data["mybillProductsData"]:
            
            productModelNo = d["productModelNo"]
            productRate = d["productRate"]
            productSize = d["productSize"]
            soldQuantity = d["productQuantity"]
           
            joma=0
            billNo=data["billNo"]
         
            with connection.cursor() as cursor_1:
                cursor_1.execute("select total from product_register where productModelNo='" +str(productModelNo) + "' and productSize='" +str(productSize) + "' order by serial desc limit 1")
                row1 = cursor_1.fetchone()
                currentTotal = row1[0]
                currentTotal -= int(soldQuantity) 
       
            with connection.cursor() as cursor_2:
                cursor_2.execute("INSERT INTO product_register(date,productModelNo,productSize,productRate,joma,total,billNo,partyName,soldQuantity,balance) VALUES ('"+str(date) + "','" +str(productModelNo) + "','" +str(
                    productSize) + "','" +str(productRate) + "','"+str(joma) + "','" + str(currentTotal) + "','"+str(billNo) + "','"+str(partyName) + "','"+str(soldQuantity) + "','"+str(currentTotal) + "')")
                connection.commit()

        with connection.cursor() as cursor_2:
            cursor_2.execute("select date, khatiyanName,joma, khoroch, balance from khatiyan_full where khatiyanName='" +str(partyName) + "' order by serial desc limit 1")
            row1 = cursor_2.fetchone()
        balance = row1[4]
        balance += int(totalAmount)
        joma = 0
        type="Party"

        with connection.cursor() as cursor_3:
            cursor_3.execute("INSERT INTO khatiyan_full(date,khatiyanName,details,joma,khoroch,balance,type) VALUES ('"+str(date) + "','" +str(partyName) + "','" +str(billNo) + "','"+str(joma) + "','"+str(totalAmount) + "','"+str(balance) + "','"+str(type) + "')")
            connection.commit()
            
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def addBillToPartyKhatiyan(request):
    if request.method == 'POST':
        shopName = request.POST.get("shopName", False)
        date = request.POST.get("date", False)
        totalAmount = request.POST.get("totalAmount", False)
        billNo=1
    
        with connection.cursor() as cursor_3:
            cursor_3.execute("INSERT INTO khatiyan_party(shopName,date,billNo,Khoroch) VALUES ('"+str(shopName) + "','"+str(
                date) + "','"+str(billNo) + "','" + str(totalAmount) + "')")
            connection.commit()
            
        with connection.cursor() as cursor_4:
            cursor_4.execute("INSERT INTO bill_totalAmountTable(shopName,date,billNo,totalAmount) VALUES ('"+str(shopName) + "','"+str(
                date) + "','"+str(billNo) + "','" + str(totalAmount) + "')")
            connection.commit()

    return HttpResponse("Hello, world. You're at the polls index.")