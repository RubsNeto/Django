from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import toDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
    ls = toDoList.objects.get(id = id)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            
            else:
                print("invalid")
            
        elif response.POST.get("deletee"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    dell = item
                    dell.delete()     

    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = toDoList(name=n)
            t.save()

            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form":form})

def view(response):
    ls = toDoList.objects.all()
    if response.method == "POST":
        if response.POST.get("deletee"):
            
            for name in ls.all():
                if response.POST.get("c" + str(name.id)) == "clicked":
                    dell = name
                    dell.delete()

    return render(response, "main/view.html", {"ls":ls})
