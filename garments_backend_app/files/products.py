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