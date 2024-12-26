from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class RegistroDiarioModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='registros_diarios')
    musculacao = models.BooleanField(default=False)
    aerobico = models.BooleanField(default=False)
    agua = models.BooleanField(default=False)
    vitaminas = models.BooleanField(default=False)
    zero_alcool = models.BooleanField(default=False)
    zero_acucar = models.BooleanField(default=False)
    zero_doces = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True, null=True)
    date_created = models.DateField(default=now)
