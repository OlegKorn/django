# Generated by Django 2.2.3 on 2019-08-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getcurrency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='nominal',
            field=models.IntegerField(),
        ),
    ]
