# Generated by Django 4.2.2 on 2023-06-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_course_incharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseparticipant',
            name='final_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courseparticipant',
            name='initial_marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
