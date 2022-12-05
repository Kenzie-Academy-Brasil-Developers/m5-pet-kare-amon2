from rest_framework import serializers
from traits.models import Trait
from rest_framework.views import status


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict):
        trait_obj, created = Trait.objects.get_or_create(**validated_data)
