from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.


# class MyException(Exception):
#     def __init__(self,msg):
#         self.msg = msg


def index_view(request):
    # context={"name":"pratik"}#setting up the view function context
    # raise MyException("Error Raised")
    return TemplateResponse(request,template="ProcessOptionalFunctionMiddlewareApp/index.html",context={"name":"pratik"})
