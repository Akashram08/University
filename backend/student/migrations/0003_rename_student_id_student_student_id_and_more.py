# Generated by Django 4.2.7 on 2023-11-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Student_Id',
            new_name='student_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
