from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
