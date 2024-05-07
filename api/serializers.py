from rest_framework import serializers

from api.models import Person, Relationship


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ["url", "first_name","last_name", "birth_date","death_date", "gender"]


class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relationship
        fields = ["url", "parent", "child", "type"]
