from django.contrib.auth.models import User

from rest_framework import serializers

from describe.models import Journal


class InsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


