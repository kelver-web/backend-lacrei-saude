from django.db import models


class Professional(models.Model):
    social_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.social_name
