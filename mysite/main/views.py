from django.shortcuts import render
from django.http import HttpResponse
from .models import toDoList, Item
# Create your views here.


def index(response, id):
    ls = toDoList.objects.get(id = id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})