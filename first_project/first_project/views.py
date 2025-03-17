from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<center><h1>hello from 1270</h1></center>")

def addition_opt(request):
    a=10
    b=10
    res=a+b
    return HttpResponse(f"Addition of {a} + {b} = {res}")

def subtraction_opt(request):
    a= 5
    b=5
    res=a-b
    return HttpResponse(f"subtraction of {a} - {b}= {res}")

def multiplication_opt(request):
    a=20
    b=9
    res = a*b
    return HttpResponse(f"multiplication of {a} * {b}= {res}")

def division_opt(request):
    a=25
    b=5
    res = a/b
    return HttpResponse(f"division of {a} / {b}={res}")
def modulus_opt(request):
    a=5
    b=5
    res = a%b
    return HttpResponse (f"modulus of {a} % {b}= {res}")
def exponentation_opt(request):
    a=2
    b=3
    res= a**b
    return  HttpResponse(f"exponentation of {a} ** {b} ={res}")
def floor_division(request):
    a=15
    b=9
    res = a//b
    return HttpResponse(f"floor division of {a} // {b} = {res}")