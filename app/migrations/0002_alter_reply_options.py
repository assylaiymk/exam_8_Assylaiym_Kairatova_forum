# Generated by Django 4.1.3 on 2022-11-12 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'Reply', 'verbose_name_plural': 'Replies'},
        ),
    ]
