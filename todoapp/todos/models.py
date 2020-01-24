from django.db.models import Model, CharField


class Todo(Model):
    title = CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.title
