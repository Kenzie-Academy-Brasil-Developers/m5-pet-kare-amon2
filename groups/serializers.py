from rest_framework import serializers
from groups.models import Group
from rest_framework.validators import UniqueValidator


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(
        max_length=50,
        validators=[
            UniqueValidator(
                queryset=Group.objects.all(), message="Scientific Name already exists"
            )
        ],
    )
    created_at = serializers.DateTimeField(read_only=True)

    # def validate_name(self, name: str) -> str:
    #     name_already_exists = Group.objects.filter(scientific_name=name).exists()
    #     if name_already_exists:
    #         raise serializers.ValidationError("Name already exists")
    #     return name
