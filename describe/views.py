from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from describe.models import Journal
from describe.serializers import InsultSerializer, UserSerializer


class InsultView(CreateModelMixin, ListModelMixin,  GenericViewSet):
    queryset = Journal.objects.all()
    serializer_class = InsultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'users':
            return User.objects.all()
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.action == 'users':
            return UserSerializer
        else:
            return self.serializer_class

    @action(methods=['create'], detail=False)
    def users(self, request):
        return self.create(request)
