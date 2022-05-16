import math

def square(value):
    return value**2


def sqrt(value):
    return "{:.4f}".format(math.sqrt(value))


def fact(value):
    facts = [1]*(value+1)
    for i in range(1, value+1):
        facts[i] = facts[i-1]*(i)
    return facts[value]


def fib(value):
    if(value == 0):
        return []
    if(value == 1):
        return [0]
    fibs = [0, 1]
    for i in range(2, value):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def calculate(type, value):
    if(type == "sq"):
        return square(value)

    elif(type == "sqrt"):
        return sqrt(value)

    elif(type == "fact"):
        return fact(value)

    elif(type == "fib"):
        return fib(value)
