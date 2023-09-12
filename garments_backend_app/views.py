

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
            print(json_data)

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
            print(json_data)

            return HttpResponse(json_data, content_type="application/json")


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
        Date = str(date.today())
        Joma = 0
        Khoroch = 0
        Balance = 0

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO user_table(Name,NID,Phone,Address,Password,Fathers_Name,Mothers_Name,Salary,Type) VALUES ('"+str(
                name) + "' ,'"+str(nid) + "','"+str(phone) + "','"+str(address) + "','"+str(password) + "','"+str(fathersName) + "','"+str(mothersName) + "','"+str(salary) + "','"+str(type) + "')")
            connection.commit()

        with connection.cursor() as cursor_2:
            cursor_2.execute("INSERT INTO khatiyan_staff(staffName,Date,Joma,Khoroch,Balance) VALUES ('"+str(
                name) + "' ,'"+str(Date) + "','"+str(Joma) + "','"+str(Khoroch) + "','"+str(Balance) + "')")
            connection.commit()

    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def getStaffKhatiyanList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select staffName, Date, Joma, Khoroch, Balance from khatiyan_staff")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('staffName', 'Date',
                    'Joma', 'Khoroch', 'Balance')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getKhatiyanDetailsStaff(request):
    if request.method == 'POST':
        staffName = request.POST.get("staffName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select Date, Joma, Khoroch, Balance from khatiyan_staff WHERE staffName='"+str(staffName)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('Date', 'Joma', 'Khoroch', 'Balance')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getProfileDetailsStaff(request):
    if request.method == 'POST':
        staffName = request.POST.get("staffName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select Name, NID, Phone, Address, Fathers_Name, Mothers_Name, Salary, Type from user_table WHERE Name='"+str(staffName)+"'")
            row1 = cursor_1.fetchone()
            result = []
            keys = ('Name', 'NID', 'Phone', 'Address',
                    'Fathes_Name', 'Mothers_Name', 'Salary', 'Type')
            result.append(dict(zip(keys, row1)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")


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

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO product_table(productModelNo,productDetails,productRate,productSize,productAvailable) VALUES ('"+str(
                productModelNo) + "','"+str(productDetails) + "','"+str(productRate) + "','"+str(productSize) + "','"+str(productAvailable) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
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
