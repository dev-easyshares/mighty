# Generated by Django 3.0.6 on 2020-05-29 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
        ('mighty', '0002_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='code',
        ),
        migrations.RemoveField(
            model_name='log',
            name='date',
        ),
        migrations.RemoveField(
            model_name='log',
            name='id',
        ),
        migrations.RemoveField(
            model_name='log',
            name='message',
        ),
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.AddField(
            model_name='log',
            name='log_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logger.Log'),
            preserve_default=False,
        ),
    ]
