# Generated by Django 3.0.7 on 2020-06-16 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0002_auto_20200616_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rator',
            new_name='rater',
        ),
    ]
