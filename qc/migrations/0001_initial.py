# Generated by Django 2.1.7 on 2019-03-23 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='qclog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('moderator_remark', models.CharField(blank=True, default='None', max_length=255, verbose_name="Moderator's Remark")),
                ('qced_on', models.DateTimeField(auto_now_add=True)),
                ('qc_status', models.BooleanField(blank=True, default=False)),
                ('qced_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='qclog_qced_by', to=settings.AUTH_USER_MODEL)),
                ('remark_from', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='qclog_remark_from', to=settings.AUTH_USER_MODEL)),
                ('video_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.youtube_videos')),
            ],
            options={
                'verbose_name': 'QC Log',
                'verbose_name_plural': 'QC Logs',
            },
        ),
    ]
