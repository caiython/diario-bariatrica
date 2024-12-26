# Generated by Django 5.1.4 on 2024-12-26 18:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroDiarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('musculacao', models.BooleanField(default=False)),
                ('aerobico', models.BooleanField(default=False)),
                ('agua', models.BooleanField(default=False)),
                ('vitaminas', models.BooleanField(default=False)),
                ('zero_alcool', models.BooleanField(default=False)),
                ('zero_acucar', models.BooleanField(default=False)),
                ('zero_doces', models.BooleanField(default=False)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(
                    default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='registros_diarios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
