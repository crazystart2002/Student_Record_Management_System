# Generated by Django 4.2.3 on 2023-08-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Recognation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face_Recognation2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_Id', models.CharField(max_length=20)),
            ],
        ),
    ]