# Generated by Django 3.2.18 on 2023-04-10 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_commend'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commend',
            new_name='Comment',
        ),
    ]