# Generated by Django 2.2.3 on 2019-07-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190719_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文html代码'),
        ),
    ]
