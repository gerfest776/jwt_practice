from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from describe.models import Journal
from describe.serializers import InsultSerializer


class InsultView(CreateModelMixin, ListModelMixin,  GenericViewSet):
    queryset = Journal.objects.all()
    serializer_class = InsultSerializer
    permission_classes = [IsAuthenticated]