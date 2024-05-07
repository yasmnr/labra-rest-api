from rest_framework import viewsets

from api.models import Choice, Question
from api.serializers import ChoiceSerializer, QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all().order_by("question")
    serializer_class = ChoiceSerializer
