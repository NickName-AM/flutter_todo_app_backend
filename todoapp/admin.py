from django.contrib import admin
from todoapp.models import Todo

# Register your models here.


## Changes attributes of a model to be displayed in admin page
## else, it uses __str__ representation described in your model,
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Todo, TodoAdmin)
