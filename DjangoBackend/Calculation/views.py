from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from Calculation.logicalFunctions import calculate
from Calculation.queryFunctions import insertCalculatedRecord, readHistory
from Calculation.utils import myCheckInt, myCheckPositive

import json

# Create your views here.


@csrf_exempt
def process(request):
    if request.method == 'POST':

        requestBody = json.loads(request.body)

        type = requestBody["type"]
        value = requestBody["value"]

        # Handling Error in input.
        if(not myCheckInt(value)):
            responseData = {
                'success': False,
                'message': "Input must be a non negative integer."
            }
            return JsonResponse(responseData, status=400)

        if(type == "sqrt" or type == "fact" or type == "fib"):
            if(not myCheckPositive(value)):
                responseData = {
                    'success': False,
                    'message': "Input must be a non negative integer for this type."
                }
                return JsonResponse(responseData, status=400)

        value = int(value)
        result = calculate(type, value)

        # Handling Error in database.
        if(not insertCalculatedRecord(type, value, result)):
            responseData = {
                'success': False,
                'message': "Internal Server Error."
            }
            return JsonResponse(responseData, status=500)

        else:
            responseData = {
                'success': True,
                'result': result
            }
            return JsonResponse(responseData, status=201)


@csrf_exempt
def getHistory(request):
    if request.method == 'POST':

        requestBody = json.loads(request.body)
        n = requestBody["n"]

        # Handling Error in input.
        if(n != ""):
            if(not myCheckInt(n)):
                responseData = {
                    'success': False,
                    'message': "Input must be a non negative integer."
                }
                return JsonResponse(responseData, status=400)

            if(not myCheckPositive(n)):
                responseData = {
                    'success': False,
                    'message': "Input must be a non negative integer."
                }
                return JsonResponse(responseData, status=400)
                
            history = readHistory(int(n))

        elif(n == ""):
            history = readHistory(n)

        # Handling Error in database.
        if(history == False):
            responseData = {
                'success': False,
                'message': "Internal Server Error."
            }
            return JsonResponse(responseData, status=500)
        else:
            responseData = {
                'success': True,
                'result': history
            }
            return JsonResponse(responseData, status=200)
