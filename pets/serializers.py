from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from traits.models import Trait
from groups.models import Group
from pets.models import PetSex, Pet
import ipdb


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    traits_count = serializers.SerializerMethodField()

    def get_traits_count(self, obj):
        return obj.traits.count()

    def create(self, validated_data: dict):
        group_dic = validated_data.pop("group")
        traits_list = validated_data.pop("traits")
        group_obj, created = Group.objects.get_or_create(**group_dic)
        pet_obj = Pet.objects.create(**validated_data, group=group_obj)

        for trait_dict in traits_list:
            trait_obj, created = Trait.objects.get_or_create(**trait_dict)
            pet_obj.traits.add(trait_obj)

        return pet_obj

    def update(self, instance: Pet, validated_data: dict):
        list = []
        traits_list = validated_data.pop("traits", None)
        if traits_list:
            for trait_dict in traits_list:
                trait_obj, created = Trait.objects.get_or_create(**trait_dict)
                list.append(trait_obj)

            instance.traits.set(list)

        group_dic = validated_data.pop("group", None)
        if group_dic:
            group_obj, created = Group.objects.get_or_create(
                scientific_name=group_dic["scientific_name"],
            )

            instance.group = group_obj

        for key, value in instance.items():
            setattr()
        return instance
