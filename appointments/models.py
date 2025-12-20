from django.db import models
from professionals.models import Professional


class Appointment(models.Model):
    date = models.DateTimeField()
    professional = models.ForeignKey(Professional, related_name='appointments',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.professional.social_name} - {self.date}"
