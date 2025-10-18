from rest_framework.generics import CreateAPIView

from users.models import User

from users.serializers import UserCreateSerializer

# Create your views here.


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        print(self.request.body)
        return super().create(request, *args, **kwargs)
