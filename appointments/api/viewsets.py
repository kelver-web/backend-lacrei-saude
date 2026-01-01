from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from appointments.models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.all()

    @action(
        detail=False,
        methods=['get'],
        url_path='by-professional/(?P<professional_id>[^/.]+)'
    )
    def by_professional(self, request, professional_id=None):
        appointments = self.get_queryset().filter(
            professional_id=professional_id
        )

        if not appointments.exists():
            raise NotFound('Nenhuma consulta encontrada')

        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)
