# Generated by Django 4.2.1 on 2023-05-09 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_test_contrent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrent',
            old_name='last_name',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='contrent',
            old_name='name',
            new_name='nombre',
        ),
    ]