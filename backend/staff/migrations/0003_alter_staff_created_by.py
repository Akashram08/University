# Generated by Django 4.2.7 on 2023-11-20 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0002_rename_staff_id_staff_staff_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
