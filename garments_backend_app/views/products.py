# Create your views here.
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse

import os
from django.conf import settings
from PIL import Image  
from django.conf import settings as django_settings

@csrf_exempt
def createProduct(request):
    if request.method == 'POST':
        productModelNo = request.POST.get("productModelNo", False)
        productDetails = request.POST.get("productDetails", False)
        productRate = request.POST.get("productRate", False)
        image = request.FILES.get('image', False)
        myimage1 = Image.open(image)
      
        fileName = str(productModelNo)+".jpg"
      
        savePath = os.path.join(django_settings.MEDIA_ROOT,fileName)
        myimage1.save(savePath)
        imagePath = "http://192.168.0.100:8000/media/"+str(fileName)


        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO product_table(productModelNo,imagePath,productDetails,productRate) VALUES ('"+str(
                productModelNo) + "','"+str(imagePath)+ "','"+str(productDetails) + "','" + str(productRate) + "')")
            connection.commit()
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        productModelNo = request.POST.get("productModelNo", False)
        productionDate = request.POST.get("productionDate", False)
        productSize = request.POST.get("productSize", False)
        productQuantity = request.POST.get("productQuantity", False)
        productRate = request.POST.get("productRate", False)
        billNo = 0
        partyName = 0
        soldQuantity = 0
       

        with connection.cursor() as cursor_1:
            cursor_1.execute("select date, productModelNo,productSize,joma,total from product_register where productModelNo='" +str(productModelNo) + "' and productSize='" +str(productSize) + "' order by serial desc limit 1")
            row1 = cursor_1.fetchone()
            
        if row1 == None:
            with connection.cursor() as cursor_1:
                cursor_1.execute("INSERT INTO product_register(date,productModelNo,productSize,productRate,joma,total,billNo,partyName,soldQuantity,balance) VALUES ('"+str(productionDate) + "','"+str(productModelNo) + "','"+str(productSize) + "','"+str(productRate) + "','"+str(productQuantity) + "','"+str(productQuantity) + "','"+str(billNo) + "','"+str(partyName) + "','"+str(soldQuantity) + "','"+str(productQuantity) + "')")
            connection.commit()
        else:
            currentTotal = row1[4]
            currentTotal += int(productQuantity) 
            with connection.cursor() as cursor_1:
                cursor_1.execute("INSERT INTO product_register(date,productModelNo,productSize,productRate,joma,total,billNo,partyName,soldQuantity,balance) VALUES ('"+str(productionDate) + "','"+str(productModelNo) + "','"+str(productSize) + "','"+str(productRate) + "','"+str(productQuantity) + "','"+str(currentTotal) + "','"+str(billNo) + "','"+str(partyName) + "','"+str(soldQuantity) + "','"+str(currentTotal) + "')")
            connection.commit()


    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def getProductsList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo,imagePath, productDetails, productRate from product_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productModelNo','imagePath','productDetails',
                    'productRate')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def getProductsAvailableList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, productSize,productRate from product_register group by productSize")
            row1 = cursor_1.fetchall()
            alldata=()
            for d in row1:
                with connection.cursor() as cursor_1:
                    cursor_1.execute("select productModelNo, productSize, total, productRate from product_register where productModelNo='"+str(d[0])+"' and productSize='"+str(d[1])+"' order by serial desc limit 1")
                    row2 = cursor_1.fetchall()
                    alldata+=row2
                
            result = []
            keys = ('productModelNo','productSize','productAvailable','productRate')
            for row in alldata:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            
        
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

            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getProductProductionDetails(request):
    productModelNo = request.POST.get("productModelNo", False)
    if request.method == 'POST':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select date, productSize, joma from product_register where productModelNo='"+str(productModelNo)+"'")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productionDate', 'productSize', 'productQuantity')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)

            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def getProductDetails(request):
    productModelNo = request.POST.get("productModelNo", False)
    if request.method == 'POST':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, imagePath, productDetails, productRate from product_table where productModelNo='"+str(productModelNo)+"'")
            row1 = cursor_1.fetchone()
            result = []
            keys = ('productModelNo', 'imagePath', 'productDetails',
                    'productRate')
            result.append(dict(zip(keys, row1)))
            json_data = json.dumps(result)
           

            return HttpResponse(json_data, content_type="application/json")
