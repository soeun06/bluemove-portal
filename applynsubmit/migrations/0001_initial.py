# Generated by Django 3.0.6 on 2021-07-03 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applymembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanted_id', models.CharField(max_length=36, null=True)),
                ('self_intro', models.TextField(max_length=500, null=True)),
                ('self_intro_len', models.IntegerField(default=0)),
                ('reason', models.TextField(max_length=500, null=True)),
                ('reason_len', models.IntegerField(default=0)),
                ('plan', models.TextField(max_length=500, null=True)),
                ('plan_len', models.IntegerField(default=0)),
                ('tracking', models.CharField(max_length=20, null=True)),
                ('tracking_reference', models.CharField(max_length=10, null=True)),
                ('tracking_etc', models.CharField(max_length=100, null=True)),
                ('portfolio', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
