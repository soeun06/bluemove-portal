# Generated by Django 3.0.6 on 2021-07-04 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0005_auto_20210704_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymembership',
            name='last_saved',
            field=models.BooleanField(default=False),
        ),
    ]
