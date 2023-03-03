from django.http import HttpResponse
from django.shortcuts import render

def user(request):
    return render(request,'home.html')

def stulogin(request):
    return render(request,'stulogin.html')

def tealogin(request):
    return render(request,'tealogin.html')

def welcome(request):
    return render(request,'welcome.html')

def zero(operation=None):
    return 0 if operation==None else operation(0)

def one(operation=None):
    return 1 if operation==None else operation(1)

def two(operation=None):
    return 2 if operation==None else operation(2)

def three(operation=None):
    return 3 if operation==None else operation(3)

def four(operation=None):
    return 4 if operation==None else operation(4)

def five(operation=None):
    return 5 if operation==None else operation(5)

def six(operation=None):
    return 6 if operation==None else operation(6)

def seven(operation=None):
    return 7 if operation==None else operation(7)

def eight(operation=None):
    return 8 if operation==None else operation(8)

def nine():
    return 9 if operation==None else operation(9)

def plus(x):
    return lambda y:y+x

def minus(x):
    return lambda y:y-x

def times(x):
    return lambda y:y*x

def dividedby(x):
    return lambda y:y/x

