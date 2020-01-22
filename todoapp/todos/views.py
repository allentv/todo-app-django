from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TodoForm
from .models import Todo
from django.views import View


class TodoManagement(View):
    form_class = TodoForm

    def get(self, request):
        todos = Todo.objects.order_by("-id")
        form = TodoForm()
        context = {"todos": todos, "form": form}

        return render(request, "todos/index.html", context=context)

    def post(self, request):
        print("Input TODO: ", request.POST["todo"])

        form = self.form_class(request.POST)
        if form.is_valid():
            new_todo = Todo(title=request.POST["todo"])
            new_todo.save()

        return HttpResponseRedirect("/")

    def delete(self, request):
        print("Deleted value : ", request.DELETE)
