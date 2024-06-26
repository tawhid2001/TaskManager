# Generated by Django 5.0.6 on 2024-06-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.TextField()),
                ('isCompleted', models.BooleanField()),
                ('taskAssignDate', models.DateField()),
            ],
        ),
    ]
