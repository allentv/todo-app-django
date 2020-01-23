from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo
from django.views import View


def landing_page(request):
    todos = Todo.objects.order_by("-id")
    form = TodoForm()
    context = {"todos": todos, "form": form}

    return render(request, "todos/index.html", context=context)


def save_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        Todo.objects.create(title=request.POST["todo"])

    return redirect("landing-page")


def delete_todo(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return redirect("landing-page")
