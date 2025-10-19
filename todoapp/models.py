from django.db import models

from users.models import User

# Create your models here.

TODO_TASK_STATUS = (
    ('incomplete', 'incomplete'),
    ('completed', 'completed')
)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(choices=TODO_TASK_STATUS, max_length=10, default='incomplete',blank=True)

    def __str__(self):
        return self.title