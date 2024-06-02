# Generated by Django 5.0.6 on 2024-06-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorName', models.CharField(max_length=30)),
                ('tasks', models.ManyToManyField(to='task.taskmodel')),
            ],
        ),
    ]