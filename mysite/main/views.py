from django.shortcuts import render
from django.http import HttpResponse
from .models import toDoList, Item
from .forms import CreateNewList
# Create your views here.


def index(response, id):
    ls = toDoList.objects.get(id = id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

#def create(response):
    #if response.method == "POST":
    #forms = CreateNewList()
    #return render(response, "main/create.html", {"form":forms})

