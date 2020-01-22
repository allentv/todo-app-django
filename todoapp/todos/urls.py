from django.urls import path, include

from .views import TodoManagement

urlpatterns = [
    path("", TodoManagement.as_view()),
]
