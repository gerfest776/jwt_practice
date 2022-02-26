from django.contrib.auth.models import User

from rest_framework import serializers

from describe.models import Journal


class InsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6)

    class Meta:
        model = User
        exclude = ('groups',
                   'user_permissions',
                   'last_login',
                   'date_joined'
                   )
