from django.utils import timezone
from rest_framework import serializers
from appointments.models import Appointment
from professionals.models import Professional


class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(
        queryset=Professional.objects.all()
    )

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'professional']

    def validate(self, data):
        if Appointment.objects.filter(
            professional=data['professional'],
            date=data['date']
        ).exists():
            raise serializers.ValidationError(
                'Já existe consulta nesse horário'
            )
        return data

    def validate_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError(
                'Data não pode ser no passado'
            )
        return value
