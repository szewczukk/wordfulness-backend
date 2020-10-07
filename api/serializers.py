from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['usertype', 'username', 'password', 'course']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(AccountSerializer, self).create(validated_data)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'
