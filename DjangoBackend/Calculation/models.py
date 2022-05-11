from django.db import models
# Create your models here.


class Algos(models.Model):
    aid = models.AutoField(primary_key=True)


class Square(Algos):
    value = models.IntegerField(null=False, blank=False)
    output = models.IntegerField(null=False)


class SquareRoot(Algos):
    value = models.IntegerField(null=False, blank=False)
    output = models.FloatField()


class Factorial(Algos):
    value = models.IntegerField(null=False, blank=False)
    output = models.IntegerField()


class Fibonacci(Algos):
    value = models.IntegerField(null=False, blank=False)
    output = models.IntegerField()


class History(models.Model):
    hisId = models.AutoField(primary_key=True)
    algoId = models.ForeignKey(Algos, on_delete=models.CASCADE)
    algoType = models.CharField(max_length=20, default=None)
