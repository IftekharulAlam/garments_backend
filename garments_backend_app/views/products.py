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
def createProduct(request):

    if request.method == 'POST':
        productModelNo = request.POST.get("productModelNo", False)
        productDetails = request.POST.get("productDetails", False)
        productRate = request.POST.get("productRate", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO product_table(productModelNo,productDetails,productRate) VALUES ('"+str(
                productModelNo) + "','"+str(productDetails) + "','" + str(productRate) + "')")
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

        with connection.cursor() as cursor_2:
            cursor_2.execute("delete from product_available_table")
            connection.commit()

        with connection.cursor() as cursor_3:
            cursor_3.execute("INSERT INTO product_available_table SELECT product_table.productModelNo, productSize, sum(product_stock.productQuantity) as productAvailable, productRate from product_table inner join product_stock on product_table.productModelNo = product_stock.productModelNo group by productSize, productModelNo")
            connection.commit()
        

    return HttpResponse("Hello, world. You're at the polls index.")

#  productModelNo, productDetails, productRate, productAvailable
@csrf_exempt
def getProductsList(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "select productModelNo, productDetails, productRate from product_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productModelNo','productDetails',
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
                "select productModelNo, productSize, productAvailable, productRate from product_available_table")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('productModelNo','productSize','productAvailable',
                    'productRate')
            for row in row1:
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
                "select productionDate, productSize, productQuantity from product_stock where productModelNo='"+str(productModelNo)+"'")
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
                "select productModelNo, productDetails, productRate from product_table where productModelNo='"+str(productModelNo)+"'")
            row1 = cursor_1.fetchone()
            result = []
            keys = ('productModelNo', 'productDetails',
                    'productRate')
            result.append(dict(zip(keys, row1)))
            json_data = json.dumps(result)

            return HttpResponse(json_data, content_type="application/json")
