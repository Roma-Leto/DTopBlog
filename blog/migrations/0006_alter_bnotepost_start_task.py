# Generated by Django 4.1.7 on 2023-03-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_bnotepost_start_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnotepost',
            name='start_task',
            field=models.DateField(blank=True, null=True, verbose_name='начало'),
        ),
    ]
