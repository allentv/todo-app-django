from django.forms import Form, CharField, TextInput


class TodoForm(Form):
    todo = CharField(
        max_length=40,
        widget=TextInput(
            attrs={"placeholder": "Enter a Todo item", "class": "form-control"}
        ),
    )
