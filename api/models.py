from django.db import models


# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    front = models.CharField(max_length=200)
    back = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return '(' + self.lesson.name + ') ' + self.front + " " + self.back
