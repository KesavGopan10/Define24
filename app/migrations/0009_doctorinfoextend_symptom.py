# Generated by Django 4.2.11 on 2024-04-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_doctorinfo_doctorinfoextend'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinfoextend',
            name='symptom',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
