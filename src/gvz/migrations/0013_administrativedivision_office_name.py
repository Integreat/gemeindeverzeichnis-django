# Generated by Django 3.2 on 2021-04-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvz', '0012_auto_20210425_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativedivision',
            name='office_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
