from rest_framework import serializers
from professionals.models import Professional


class ProfessionalSerializer(serializers.ModelSerializer):
    social_name = serializers.CharField(max_length=255)
    class Meta:
        model = Professional
        fields = ['id', 'social_name', 'profession', 'address', 'contact']

    def validate_social_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                'Nome social não pode ser vazio'
            )
        return value
