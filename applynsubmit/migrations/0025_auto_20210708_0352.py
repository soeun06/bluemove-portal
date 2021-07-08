# Generated by Django 3.0.6 on 2021-07-08 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0024_auto_20210708_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymembership',
            name='joined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applymembership',
            name='notified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('미선발', '미선발'), ('미결정', '미결정'), ('선발', '선발')], default='미결정', max_length=5, null=True),
        ),
    ]
