# Generated by Django 3.0.6 on 2021-07-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0003_remove_applymembership_failed'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymembership',
            name='failed',
            field=models.BooleanField(default=False),
        ),
    ]
