from django.urls import path, include

from .views import landing_page, save_todo, delete_todo

urlpatterns = [
    path("", landing_page, name="landing-page"),
    path("add/", save_todo, name="save-todo"),
    path("remove/<int:todo_id>", delete_todo, name="delete-todo"),
]
