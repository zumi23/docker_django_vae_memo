# Generated by Django 3.2.14 on 2023-03-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homecontents',
            name='action',
            field=models.CharField(max_length=255, null=True),
        ),
    ]