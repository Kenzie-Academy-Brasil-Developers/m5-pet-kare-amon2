from rest_framework import serializers
from traits.models import Trait
from rest_framework.views import status


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)

    # def validate_name(self, name: str) -> str:
    #     name_already_exists = Trait.objects.filter(name=name).exists()
    #     if name_already_exists:
    #         raise serializers.ValidationError("Trait already exists")
    #     return name
    def create(self, validated_data: dict):
        trait_obj, created = Trait.objects.get_or_create(**validated_data)
        if not created:
            raise ValueError({"message": "trait already exists"}, 409)
