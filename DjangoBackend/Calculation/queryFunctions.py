from asyncio import log
from logging import WARNING
import sqlite3

from Calculation.models import Square, SquareRoot, Factorial, Fibonacci, History
from Calculation.serializers import SquareSerializer, SquareRootSerializer, FactorialSerializer, FibonacciSerializer


def insertCalculatedRecord(type, value, result):
    if(type == 'sq'):
        try:
            squareInstance = Square(value=value, output=result)
            squareInstance.save()
            algoInstance = Square.objects.get(aid=squareInstance.aid)
            History.objects.create(algoId=algoInstance, algoType=type)
            return True
        except sqlite3.Error as err:
            log(WARNING,
                f'There was an error creating the square related record in the database: {err}')
            return False

    elif(type == 'sqrt'):
        try:
            squareRootInstance = SquareRoot(value=value, output=result)
            squareRootInstance.save()
            algoInstance = SquareRoot.objects.get(aid=squareRootInstance.aid)
            History.objects.create(algoId=algoInstance, algoType=type)
            return True
        except sqlite3.Error as err:
            log(WARNING,
                f'There was an error creating the sqrt related record in the database: {err}')
            return False

    elif(type == 'fact'):
        try:
            factorialInstance = Factorial(value=value, output=result)
            factorialInstance.save()
            algoInstance = Factorial.objects.get(aid=factorialInstance.aid)
            History.objects.create(algoId=algoInstance, algoType=type)
            return True
        except sqlite3.Error as err:
            log(WARNING,
                f'There was an error creating the factorial related record in the database: {err}')
            return False

    elif(type == 'fib'):
        try:
            fibonacciInstance = Fibonacci(value=value, output=result)
            fibonacciInstance.save()
            algoInstance = Fibonacci.objects.get(aid=fibonacciInstance.aid)
            History.objects.create(algoId=algoInstance, algoType=type)
            return True
        except sqlite3.Error as err:
            log(WARNING,
                f'There was an error creating the fibonacci related record in the database: {err}')
            return False


def readHistory(n):
    try:

        if(n == ""):
            history = History.objects.all().order_by('-hisId')
        else:
            history = History.objects.all().order_by('-hisId')[:n]

        historyList = []
        for p in history.values():

            if(p['algoType'] == 'sq'):
                historyElement = Square.objects.filter(aid=p['algoId_id'])
                historyElementSerializer = SquareSerializer(
                    historyElement, many=True)
                dataDict = historyElementSerializer.data[0]
                dataDict['type'] = 'Square'
                historyList.append(dataDict)

            elif(p['algoType'] == 'sqrt'):
                historyElement = SquareRoot.objects.filter(
                    aid=p['algoId_id'])
                historyElementSerializer = SquareRootSerializer(
                    historyElement, many=True)
                dataDict = historyElementSerializer.data[0]
                dataDict['type'] = 'SquareRoot'
                historyList.append(dataDict)

            elif(p['algoType'] == 'fact'):
                historyElement = Factorial.objects.filter(
                    aid=p['algoId_id'])
                historyElementSerializer = FactorialSerializer(
                    historyElement, many=True)
                dataDict = historyElementSerializer.data[0]
                dataDict['type'] = 'Factorial'
                historyList.append(dataDict)
                
            elif(p['algoType'] == 'fib'):
                historyElement = Fibonacci.objects.filter(
                    aid=p['algoId_id'])
                historyElementSerializer = FibonacciSerializer(
                    historyElement, many=True)
                dataDict = historyElementSerializer.data[0]
                dataDict['type'] = 'Fibonacci'
                historyList.append(dataDict)

        return historyList

    except sqlite3.Error as err:
        log(WARNING,
            f'There was an error reading history table from database: {err}')
        return False
