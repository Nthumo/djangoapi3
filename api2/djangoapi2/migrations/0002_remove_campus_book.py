# Generated by Django 5.0.6 on 2024-07-02 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='book',
        ),
    ]