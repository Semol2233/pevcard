# Generated by Django 2.2.5 on 2021-09-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0004_auto_20210920_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_overtime',
            name='over_hour_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
