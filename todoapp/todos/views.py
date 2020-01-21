from django.shortcuts import render

from .models import Todo
from django.views import View


class LandingPage(View):
    def get(self, request):
        todos = Todo.objects.order_by("-id")
        context = {"todos": todos}

        return render(request, "todos/index.html", context=context)
