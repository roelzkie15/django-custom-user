# Generated by Django 2.0.2 on 2018-02-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
