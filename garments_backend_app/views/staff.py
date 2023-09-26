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
def getStaffList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select Name, NID from user_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('Name', 'NID')
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

            return HttpResponse(json_data, content_type="application/json")