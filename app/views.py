from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import decorators as dec

@dec.api_view(['GET'])
def view(request):
    
    class Exc(Exception):
        pass
    
    raise Exc
    
    return Response('Ok')


from django.http import HttpResponse

def regular(request):
    return HttpResponse('Ok')