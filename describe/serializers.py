from rest_framework import serializers

from describe.models import Journal


class InsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

