from rest_framework import viewsets

from .serializers import *
from .models import *


# Create your views here.
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('created')
    serializer_class = LessonSerializer


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        queryset = Flashcard.objects.all()
        lesson = self.request.query_params.get('lesson')

        if lesson:
            queryset = queryset.filter(lesson=lesson)

        return queryset
