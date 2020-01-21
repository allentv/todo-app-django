from django.contrib.admin import register, ModelAdmin

from .models import Todo


@register(Todo)
class TodoAdmin(ModelAdmin):
    pass
