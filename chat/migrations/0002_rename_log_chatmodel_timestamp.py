# Generated by Django 4.2.3 on 2023-07-30 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmodel',
            old_name='log',
            new_name='timestamp',
        ),
    ]
