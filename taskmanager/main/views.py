from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task, Items
# Create your views here.
from .models import Task
def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    tasks = Task.objects.all().order_by('id')
    return render(request, 'main/tasks.html', {
        "title": "Нужно выполнить",
        "tasks": tasks
    })

def call(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Форма была заполнена неверно!'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, "main/call.html", context )


def items(request):
    objects = Items.objects.all()
    price = Items.price
    image = Items.image
    description = Items.description
    actors = Items.actors
    context1 = {

        'titles': objects,
        'price': price,
        'image':image,
        'description': description,
        'actors': actors
    }
    return render(request, "main/items.html", context1)