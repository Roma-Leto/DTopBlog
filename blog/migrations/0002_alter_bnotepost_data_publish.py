# Generated by Django 4.1.7 on 2023-03-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bnotepost',
            name='data_publish',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата'),
        ),
    ]
