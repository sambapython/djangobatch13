# Generated by Django 3.0.2 on 2020-01-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
