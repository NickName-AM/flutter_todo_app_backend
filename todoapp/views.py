from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import DestroyAPIView


from todoapp.models import Todo
from todoapp.serializers import TodoListCreateSerializer

# Create your views here.


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListCreateSerializer

    def post(self, request, *args, **kwargs):
        print(self.request.body)
        return super().post(request, *args, **kwargs)

class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()