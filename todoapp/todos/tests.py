from django.test import TestCase
from django.test import Client

from todos.models import Todo


class TodoTestCase(TestCase):
    client = Client()

    def tearDown(self):
        Todo.objects.all().delete()

    def test_add_todo(self):
        self.client.post("/add/", {"todo": "A New Task"})
        self.assertEqual(Todo.objects.count(), 1)

    def test_delete_todo(self):
        new_todo = Todo.objects.create(title="Test ToDo")
        self.client.delete("/remove/{}/".format(new_todo.id))
        self.assertEqual(Todo.objects.count(), 0)

    def test_list_todos(self):
        todo_items = ["Test ToDo1", "Test ToDo2", "Test ToDo3"]
        for item in todo_items:
            Todo.objects.create(title=item)

        created_todos = self.client.get("").context["todos"]

        self.assertListEqual(todo_items, sorted([todo.title for todo in created_todos]))

    def test_will_display_title_when_printed(self):
        new_todo = Todo.objects.create(title="Test ToDo")
        self.assertEqual("Test ToDo", str(new_todo))
