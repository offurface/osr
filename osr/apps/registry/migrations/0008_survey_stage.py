# Generated by Django 2.2.6 on 2019-11-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0007_auto_20191030_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='stage',
            field=models.CharField(blank=True, choices=[('1 этап', '1 этап'), ('2 этап', '2 этап'), ('3 этап', '3 этап')], max_length=15, null=True, verbose_name='Этап'),
        ),
    ]
