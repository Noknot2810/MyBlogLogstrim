# Generated by Django 3.2.5 on 2021-07-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
