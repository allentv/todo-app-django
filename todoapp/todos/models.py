from django.db.models import Model, BooleanField, CharField, DateTimeField


class Todo(Model):
    title = CharField(max_length=1024, null=False, blank=False)
    completed = BooleanField(default=False)
    created = DateTimeField(auto_now=True)
    updated = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
