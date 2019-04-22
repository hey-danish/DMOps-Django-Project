# Generated by Django 2.1.7 on 2019-04-10 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='actors',
        ),
        migrations.AddField(
            model_name='title',
            name='actor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='title',
            name='actress',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='title',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='title_language', to='generic.Language'),
        ),
    ]