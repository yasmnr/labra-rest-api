from rest_framework import viewsets

from api.models import Relationship, Person
from api.serializers import RelationshipSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all().order_by("parent")
    serializer_class = RelationshipSerializer
