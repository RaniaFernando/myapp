# Generated by Django 5.1 on 2024-08-25 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('year_of_delivery', models.IntegerField()),
                ('semester_of_delivery', models.IntegerField(choices=[(1, 'First'), (2, 'Second')])),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'First'), (2, 'Second')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_management.course')),
            ],
        ),
    ]
