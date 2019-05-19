# Generated by Django 2.2 on 2019-04-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='File')),
                ('name', models.CharField(max_length=50, verbose_name='檔名')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
