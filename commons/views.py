from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("FUNCIONA")
# Create your views here.
