from rest_framework import serializers

from .models import *


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class FlashcardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'
