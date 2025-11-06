from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse('hello world')
def sample1(reruest):
    return HttpResponse('welocome to dijango')
def sampleinfo(request):
    # data={"name":"aneela","age":23}
    data={"result":[4,6,8,9]}
    return JsonResponse(data)
def dynamicresponse(request):
    name=request.GET.get("name","krishna")
    city=request.GET.get("city","hyd")
    return HttpResponse(f"hello {name} from {city}")
def sum(request):
    a=2
    b=3
    sum=a+b
    return HttpResponse(sum)
def sub(request):
    x=20
    y=10
    sub=x-y
    return HttpResponse(sub)
def mult(request):
    c=20
    d=5
    mult=c*d
    return HttpResponse(mult)

def sum1(request):
    a= request.GET.get('a',10)
    b=request.GET.get('b',20)
    result = a + b
    return HttpResponse(f"The sum1 is: {result}")
def mult1(request):
    x=request.GET.get('x',10)
    y=request.GET.get('y',20)
    result=x*y
    return HttpResponse(f"the mult1 is:{result}")
def sub1(request):
    c=request.GET.get('c',80)
    d=request.GET.get('d',20)
    result1=c-d
    return HttpResponse(f"the sub1 is:{result1}")


    