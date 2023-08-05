from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate():
    x=1
    y=2
    return x

def say_hello(request):
    return render(request,'hello.html',{'name':'vignesh'})

def arithmetic(request):
    op = str(request.POST['operation'])
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    if op == 'add':
        res = val1+val2
    elif op=='subtract':
        res = val1-val2
    elif op=='multiply':
        res = val1*val2
    elif op=='divide':
        res = val1/val2
    else:
        res = 'invalid operation'
    
    return render(request,"result.html",{'result' : res})