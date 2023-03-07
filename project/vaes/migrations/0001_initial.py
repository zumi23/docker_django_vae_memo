# Generated by Django 3.2.14 on 2023-02-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('n_z', models.IntegerField()),
                ('n_layer', models.IntegerField()),
                ('n_count', models.IntegerField()),
                ('rep', models.FloatField()),
                ('dr', models.FloatField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'nets',
            },
        ),
    ]
