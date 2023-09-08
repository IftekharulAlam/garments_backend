

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
        if userType == "HomeOwner":
            with connection.cursor() as cursor_1:
                cursor_1.execute(
                    "select Name, Address, Phone, profilePic, Password from homeowner where name='"+str(name) + "'")
                row1 = cursor_1.fetchone()
            if row1 == None:
                data = {"message": "Wrong"}
                result = []
                result.append(data)
                json_data = json.dumps(result)
                return HttpResponse(json_data, content_type="application/json")
            else:
                if name == row1[0] and password == row1[4]:
                    # data = {"message": "Success"}
                    result = []
                    keys = ('name', 'address', 'phone',
                            'profilePic', 'password')

                    im = row1[3]
                    base64_string = im.decode('utf-8')
                    y = list(row1)
                    y[3] = base64_string
                    row1 = tuple(y)
                    result.append(dict(zip(keys, row1)))
                    json_data = json.dumps(result)
                    return HttpResponse(json_data, content_type="application/json")
                else:
                    data = {"message": "Wrong"}
                    result = []
                    result.append(data)
                    json_data = json.dumps(result)
                    return HttpResponse(json_data, content_type="application/json")

        else:
            with connection.cursor() as cursor_1:
                cursor_1.execute(
                    "select Name, Address, Phone, profilePic, workingHour, Password from worker_table where name='"+str(name)+"'")
                row1 = cursor_1.fetchone()
                # print(row1)

            if row1 == None:
                data = {"message": "Wrong"}
                result = []
                result.append(data)
                json_data = json.dumps(result)
                return HttpResponse(json_data, content_type="application/json")
            else:
                if name == row1[0] and password == row1[5]:
                    # data = {"message": "Success"}
                    result = []
                    keys = ('name', 'address', 'phone',
                            'profilePic', 'workingHour', 'Password')
                    im = row1[3]
                    base64_string = im.decode('utf-8')
                    y = list(row1)
                    y[3] = base64_string
                    row1 = tuple(y)
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
