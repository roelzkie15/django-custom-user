# Generated by Django 2.0.2 on 2018-02-09 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('default_account', '0003_auto_20180209_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
