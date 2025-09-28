from rest_framework import serializers

from todoapp.models import Todo

# Serializers

class TodoListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        # fields = ['title', 'date', 'start_time', 'end_time']
        exclude = ['id']