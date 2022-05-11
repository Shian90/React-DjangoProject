from django.db import models
from rest_framework import serializers

from Calculation.models import Algos, Square, SquareRoot, Factorial, Fibonacci, History


class AlgosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algos
        fields = ('aid')


class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Square
        fields = ('value', 'output')


class SquareRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = SquareRoot
        fields = ('value', 'output')


class FactorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factorial
        fields = ('value', 'output')


class FibonacciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fibonacci
        fields = ('value', 'output')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('hisId', 'algoId', 'algoType')
