# Generated by Django 5.1.3 on 2024-12-05 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.RemoveField(
            model_name='book',
            name='library_id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='library_id',
        ),
    ]
