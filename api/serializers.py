from rest_framework import serializers

from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['usertype', 'username', 'password']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'
