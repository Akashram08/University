# Generated by Django 4.2.7 on 2023-11-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
