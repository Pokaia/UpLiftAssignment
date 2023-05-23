from rest_framework import serializers
from providers.models import Provider, Skill, ProviderSkill


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
                'id',
                'first_name',
                'last_name',
                'sex',
                'birth_date',
                'rating',
                'company',
                'active',
                'country',
                'language',
                ]
