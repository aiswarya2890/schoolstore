# Generated by Django 4.1.1 on 2023-01-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0002_student_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_form',
            name='MATERIAL',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]