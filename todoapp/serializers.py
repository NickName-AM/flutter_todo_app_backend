from rest_framework import serializers

from todoapp.models import Todo

# Serializers

class TodoListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'
        # exclude = ['id']