from django.shortcuts import render
from django.http import HttpResponse
from .models import toDoList, Item
# Create your views here.


def index(response, id):
    ls = toDoList.objects.get(id = id)
    return HttpResponse("<h1>%s</h1>" %ls.name)

def v1(response):
    return HttpResponse("<h1>Screen 1!</h1>")
