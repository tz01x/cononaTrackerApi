# Generated by Django 2.2 on 2020-04-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangla', '0003_auto_20200415_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
