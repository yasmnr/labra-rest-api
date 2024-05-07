from rest_framework import serializers

from api.models import Person, Relationship


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            "url",
            "first_name",
            "last_name",
            "birth_date",
            "death_date",
            "gender",
        ]


class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    parent_name = serializers.SerializerMethodField()
    child_name = serializers.SerializerMethodField()

    class Meta:
        model = Relationship
        fields = ["url", "parent", "child", "type", "parent_name", "child_name"]

    def get_parent_name(self, obj):
        return str(obj.parent)

    def get_child_name(self, obj):
        return str(obj.child)
