from rest_framework import serializers

from todoapp.models import Todo

# Serializers

class TodoListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = ['user']
    
    def create(self, validated_data):
        request = self.context.get('request')
        todo = Todo.objects.create(user=request.user, **validated_data)
        return todo