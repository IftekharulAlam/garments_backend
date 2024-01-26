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
def getPartyKhatiyanDetails(request):
    if request.method == 'POST':
        shopName = request.POST.get("shopName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, billNo, Joma, Khoroch, Balance from khatiyan_party WHERE shopName='"+str(shopName)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ("date", "billNo", "joma", "khoroch", "balance")
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)


            return HttpResponse(json_data, content_type="application/json")
        
@csrf_exempt
def createParty(request):
    if request.method == 'POST':
        ownerName = request.POST.get("ownerName", False)
        shopName = request.POST.get("shopName", False)
        ownerPhone = request.POST.get("ownerPhone", False)
        ownerAddress = request.POST.get("ownerAddress", False)
        shopAddress = request.POST.get("shopAddress", False)
        shopPhone = request.POST.get("shopPhone", False)
        Date = request.POST.get("datetime", False)

    
        Joma = 0
        Khoroch = 0
        Balance = 0
        billNo = 0

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO party_profile(ownerName,shopName,ownerPhone,ownerAddress,shopAddress,shopPhone) VALUES ('"+str(
                ownerName) + "' ,'"+str(shopName) + "','"+str(ownerPhone) + "','"+str(ownerAddress) + "','"+str(shopAddress) + "','"+str(shopPhone) + "')")
            connection.commit()

        with connection.cursor() as cursor_2:
            cursor_2.execute("INSERT INTO khatiyan_party(shopName,date,billNo,Joma,Khoroch,Balance) VALUES ('"+str(
                shopName) + "','" + str(Date) + "','" + str(billNo) + "','" + str(Joma) + "','" + str(Khoroch) + "','" + str(Balance) + "')")
            connection.commit()

    return HttpResponse("Hello, world. You're at the polls index.")