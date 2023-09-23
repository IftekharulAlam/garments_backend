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


            return HttpResponse(json_data, content_type="application/json")



