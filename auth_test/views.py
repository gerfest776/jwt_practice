from django.contrib.auth.models import User

from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from auth_test.serializers import RegisterSerializer


class RegisterView(CreateModelMixin,
                   GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
