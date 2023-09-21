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
def createDailysheetJoma(request):
    if request.method == 'POST':
        datetime = request.POST.get("datetime", False)
        listOFItem = request.POST.get("listOFItem", False)
        listOFAmount = request.POST.get("listOFAmount", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO dailySheetjoma_table(date,item,amount) VALUES ('"+str(
                datetime) + "','"+str(listOFItem) + "','"+str(listOFAmount) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def createDailysheetKhoroch(request):
    if request.method == 'POST':
        datetime = request.POST.get("datetime", False)
        listOFItem = request.POST.get("listOFItem", False)
        listOFAmount = request.POST.get("listOFAmount", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO dailySheetKhoroch_table(date,item,amount) VALUES ('"+str(
                datetime) + "','"+str(listOFItem) + "','"+str(listOFAmount) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def dailysheetJomaKhorochList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, item from dailySheetKhoroch_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('date', 'item')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)

            return HttpResponse(json_data, content_type="application/json")


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
def getPartyKhatiyanDetails(request):
    if request.method == 'POST':
        shopName = request.POST.get("shopName", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, billNo, Joma, Khoroch, Balance from khatiyan_party WHERE shopName='"+str(shopName)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('Date', 'billNo', 'Joma', 'Khoroch', 'Balance')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)

            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getPartyList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select ownerName, shopName, ownerPhone, ownerAddress, shopAddress, shopPhone from party_profile")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('ownerName', 'shopName',
                    'ownerPhone', 'ownerAddress', 'shopAddress', 'shopPhone')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)

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

        Date = str(date.today())
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
        
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO product_table(productModelNo,productDetails,productRate,productAvailable) VALUES ('"+str(
                productModelNo) + "','"+str(productDetails) + "','"+str(productRate) + "','"+str(productAvailable) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        productModelNo = request.POST.get("productModelNo", False)
        productionDate = request.POST.get("productionDate", False)
        productSize = request.POST.get("productSize", False)
        productQuantity = request.POST.get("productQuantity", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO product_stock(productModelNo,productionDate,productSize,productQuantity) VALUES ('"+str(
                productModelNo) + "','"+str(productionDate) + "','"+str(productSize) + "','"+str(productQuantity) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def getProductsList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, productDetails, productRate, productAvailable from product_table GROUP BY productModelNo")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productModelNo', 'productDetails',
                    'productRate', 'productAvailable')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getProductsSizeList(request):
    productModelNo = request.POST.get("productModelNo", False)
    if request.method == 'POST':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, productSize from product_table where productModelNo='"+str(productModelNo)+"' GROUP BY productSize")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productModelNo', 'productSize')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def getProductProductionDetails(request):
    productModelNo = request.POST.get("productModelNo", False)
    if request.method == 'POST':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productionDate, productSize, productQuantity from product_stock where productModelNo='"+str(productModelNo)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productionDate', 'productSize', 'productQuantity')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")
        
@csrf_exempt
def getProductDetails(request):
    productModelNo = request.POST.get("productModelNo", False)
    if request.method == 'POST':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, productDetails, productRate, productAvailable from product_table where productModelNo='"+str(productModelNo)+"'")
            row1 = cursor_1.fetchone()
            result = []
            keys = ('productModelNo','productDetails', 'productRate', 'productAvailable')
            result.append(dict(zip(keys, row1)))
            json_data = json.dumps(result)
            print(json_data)
            return HttpResponse(json_data, content_type="application/json")