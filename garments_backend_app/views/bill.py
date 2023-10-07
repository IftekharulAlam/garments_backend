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
        shopName = request.POST.get("shopName", False)
        date = request.POST.get("date", False)
        productModelNo = request.POST.get("listOFProductModelNo", False)
        productRate = request.POST.get("listOFProductRate", False)
        productSize = request.POST.get("listOFProductSize", False)
        productQuantity = request.POST.get("listOFProductQuantity", False)
        totalAmount = request.POST.get("totalAmount", False)
        billNo=1
       
        with connection.cursor() as cursor_2:
            cursor_2.execute("INSERT INTO bill(BillNo, date,shopName,productModelNo,productRate,productSize,productQuantity) VALUES ('"+str(billNo) + "','" +str(date) + "','" +str(
                shopName) + "','" +str(productModelNo) + "','"+str(productRate) + "','" + str(productSize) + "','"+str(productQuantity) + "')")
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