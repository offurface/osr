# Generated by Django 2.2.6 on 2019-11-11 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0009_auto_20191108_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='primary',
            old_name='body_type_mather',
            new_name='body_type_mother',
        ),
        migrations.RenameField(
            model_name='primary',
            old_name='height_mather',
            new_name='height_mother',
        ),
        migrations.RenameField(
            model_name='primary',
            old_name='weight_mather',
            new_name='weight_mother',
        ),
    ]