# Generated by Django 2.2.3 on 2019-07-19 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20190717_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
