# Generated by Django 3.2.14 on 2023-02-14 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaes', '0004_auto_20230208_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenImgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_all_imgpath', models.CharField(max_length=255, null=True)),
                ('label_0_imgpath', models.CharField(max_length=255, null=True)),
                ('label_1_imgpath', models.CharField(max_length=255, null=True)),
                ('label_2_imgpath', models.CharField(max_length=255, null=True)),
                ('label_3_imgpath', models.CharField(max_length=255, null=True)),
                ('label_4_imgpath', models.CharField(max_length=255, null=True)),
                ('label_5_imgpath', models.CharField(max_length=255, null=True)),
                ('label_6_imgpath', models.CharField(max_length=255, null=True)),
                ('label_7_imgpath', models.CharField(max_length=255, null=True)),
                ('label_8_imgpath', models.CharField(max_length=255, null=True)),
                ('label_9_imgpath', models.CharField(max_length=255, null=True)),
                ('net', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaes.nets')),
            ],
            options={
                'db_table': 'gen_imgs',
            },
        ),
        migrations.CreateModel(
            name='NetFigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_figpath', models.CharField(max_length=255, null=True)),
                ('dr_figpath', models.CharField(max_length=255, null=True)),
                ('dr_rep_figpath', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'net_figs',
            },
        ),
        migrations.RemoveField(
            model_name='netfigures',
            name='net',
        ),
        migrations.DeleteModel(
            name='GeneratedImages',
        ),
        migrations.DeleteModel(
            name='NetFigures',
        ),
    ]
