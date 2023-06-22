# Generated by Django 4.2.2 on 2023-06-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='couse_code',
            field=models.CharField(default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
