# Generated by Django 2.0.4 on 2018-04-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
