# Generated by Django 3.0.6 on 2021-07-07 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applynsubmit', '0018_auto_20210707_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('미결정', '미결정'), ('선발', '선발'), ('미선발', '미선발')], default='미결정', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='applymembershipnoti',
            name='saved_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
