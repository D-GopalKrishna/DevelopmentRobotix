# Generated by Django 2.1.7 on 2020-02-16 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roboPortal', '0009_auto_20200215_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='member',
        ),
        migrations.AddField(
            model_name='team',
            name='member1',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='member1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]