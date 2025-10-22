from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todoapp.models import Todo
from todoapp.serializers import TodoListCreateSerializer

from users.permissions import IsOwner

# Create your views here.


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('date')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
