# Generated by Django 3.2.21 on 2023-12-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_auto_20231227_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='session_record_table',
            name='check',
            field=models.TextField(default='absent'),
        ),
    ]
