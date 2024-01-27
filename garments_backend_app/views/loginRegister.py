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
def login(request):
    if request.method == 'POST':
        name = request.POST.get("name", False)
        password = request.POST.get("password", False)
        userType = request.POST.get("userType", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select Name, Address, Phone, Password from user_table where name='"+str(name) + "'")
            row1 = cursor_1.fetchone()
        if row1 == None:
            data = {"message": "Wrong"}
            result = []
            result.append(data)
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")
        else:
            if name == row1[0] and password == row1[3]:
                # data = {"message": "Success"}
                result = []
                keys = ('name', 'address', 'phone',
                        'password')
                result.append(dict(zip(keys, row1)))
                json_data = json.dumps(result)
                return HttpResponse(json_data, content_type="application/json")
            else:
                data = {"message": "Wrong"}
                result = []
                result.append(data)
                json_data = json.dumps(result)
                return HttpResponse(json_data, content_type="application/json")
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get("name", False)
        address = request.POST.get("address", False)
        phone = request.POST.get("phone", False)
        nid = request.POST.get("nid", False)
        password = request.POST.get("password", False)
        Date = request.POST.get("date", False)
        salary = request.POST.get("salary", False)
        type = request.POST.get("type", False)
      
        Joma = 0
        Khoroch = 0
        Balance = 0
        Details = 0
        type = "Staff"

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO user_table(Name,NID,Phone,Address,Password,Salary,Type) VALUES ('"+str(
                name) + "' ,'"+str(nid) + "','"+str(phone) + "','"+str(address) + "','"+str(password) +"','" +str(salary) + "','"+str(type) + "')")
            connection.commit()

        with connection.cursor() as cursor_2:
            cursor_2.execute("INSERT INTO khatiyan_full(Date,khatiyanName,details,joma,khoroch,balance,type) VALUES ('"+str(
                Date) + "','"+str(name) +"','"+str(Details) + "','"+str(Joma) + "','"+str(Khoroch) + "','"+str(Balance) + "','"+str(type) + "')")
            connection.commit()

    return HttpResponse("Hello, world. You're at the polls index.")