# Generated by Django 2.1.7 on 2019-04-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfms', '0003_auto_20190409_1156'),
        ('raci', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_ownership',
            name='contract_id_fk',
            field=models.ManyToManyField(to='cfms.Contract'),
        ),
    ]