# Generated by Django 4.2.7 on 2023-11-22 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0003_alter_staff_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staff_modified', to=settings.AUTH_USER_MODEL),
        ),
    ]
