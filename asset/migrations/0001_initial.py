# Generated by Django 2.1.7 on 2019-03-23 10:59

import asset.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generic', '0001_initial'),
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(default=asset.models.Album.get_autogenerated_code, editable=False, max_length=8)),
                ('upc_code', models.CharField(blank=True, default='NA', max_length=15)),
                ('album_name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generic.Genres_List')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=asset.models.Title.get_autogenerated_code, editable=False, max_length=8)),
                ('isrc_code', models.CharField(blank=True, default='NA', max_length=15)),
                ('display_name', models.CharField(max_length=150)),
                ('cloud_path', models.CharField(blank=True, max_length=250)),
                ('mood', models.CharField(blank=True, max_length=50)),
                ('sequence', models.IntegerField(blank=True, default=0)),
                ('label', models.CharField(blank=True, max_length=100)),
                ('duration_sec', models.IntegerField(blank=True, default=0, verbose_name='Play Duration in Seconds')),
                ('acquisition_cost', models.FloatField(blank=True, default=0.0, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('director', models.CharField(blank=True, max_length=100)),
                ('producer', models.CharField(blank=True, max_length=100)),
                ('actors', models.CharField(blank=True, max_length=200)),
                ('actress', models.CharField(blank=True, max_length=200)),
                ('singer', models.CharField(blank=True, max_length=200)),
                ('lyricist', models.CharField(blank=True, max_length=200)),
                ('music_composer', models.CharField(blank=True, max_length=200)),
                ('content_provider', models.CharField(blank=True, max_length=100)),
                ('deep_link', models.CharField(blank=True, max_length=200)),
                ('purchase_date', models.DateField(blank=True, default=datetime.date.today)),
                ('origin_country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('origin_country_state', models.CharField(blank=True, max_length=60)),
                ('status', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generic.Genres_List')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generic.Language')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extras.Partner')),
                ('sub_genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='track_sub_genre', to='generic.Genres_List')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='generic.Asset_Type')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='titles',
            field=models.ManyToManyField(to='asset.Title'),
        ),
    ]
