# Generated by Django 2.1.7 on 2019-04-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190418_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='catagory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='facebook',
            name='sub_catagory',
            field=models.CharField(max_length=100),
        ),
    ]
