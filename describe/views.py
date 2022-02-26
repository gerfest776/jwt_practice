from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet

from describe.models import Journal
from describe.serializers import InsultSerializer, UserSerializer


class InsultView(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Journal.objects.all()
    serializer_class = InsultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'users_post' or self.action == 'users_get':
            return User.objects.all()
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.action == 'users_post' or self.action == 'users_get':
            return UserSerializer
        else:
            return self.serializer_class

    @action(methods=['get'], detail=False)
    def users_get(self, request):
        return self.list(request)
