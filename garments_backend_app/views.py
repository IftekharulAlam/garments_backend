

# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse


@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        name = request.POST.get("name", False)
        address = request.POST.get("address", False)
        phone = request.POST.get("phone", False)
        nid = request.POST.get("nid", False)
        password = request.POST.get("password", False)
        fathersName = request.POST.get("fathersName", False)
        mothersName = request.POST.get("mothersName", False)
        salary = request.POST.get("salary", False)
        type = request.POST.get("type", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO user_table(Name,NID,Phone,Address,Password,Fathers_Name,Mothers_Name,Salary,Type) VALUES ('"+str(
                name) + "' ,'"+str(nid) + "','"+str(phone) + "','"+str(address) + "','"+str(password) + "','"+str(fathersName) + "','"+str(mothersName) + "','"+str(salary) + "','"+str(type) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


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
def createProduct(request):
    productAvailable = "0"
    if request.method == 'POST':
        productModelNo = request.POST.get("productModelNo", False)
        productDetails = request.POST.get("productDetails", False)
        productRate = request.POST.get("productRate", False)
        productSize = request.POST.get("productSize", False)
        # productAvailable = request.POST.get("productAvailable", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO product_table(productModelNo,productDetails,productRate,productSize,productAvailable) VALUES ('"+str(
                productModelNo) + "','"+str(productDetails) + "','"+str(productRate) + "','"+str(productSize) + "','"+str(productAvailable) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


def getProductsList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, productDetails, productRate, productSize, productAvailable from product_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productModelNo', 'productDetails',
                    'productRate', 'productSize', 'productAvailable')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")
