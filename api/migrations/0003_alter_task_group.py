# Generated by Django 4.1.1 on 2022-09-25 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_task_description_alter_task_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.group'),
        ),
    ]
