# Generated by Django 3.0.6 on 2020-05-16 13:23

from django.db import migrations, models
import mighty.models
import mighty.models.base
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mighty', '0004_auto_20200514_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', mighty.models.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('graphtype', models.CharField(choices=[('BAR', 'Bar'), ('BIPOLAR', 'Bipolar'), ('FUNNEL', 'Funnel'), ('GAUGE', 'Gauge'), ('HORIZONTALBAR', 'Horizontal Bar'), ('HORIZONTALPROGRESSBARS', 'Horizontal Progress bars'), ('LINE', 'Line'), ('PIE', 'Pie'), ('RADAR', 'Radar'), ('ROSE', 'Rose'), ('SCATTER', 'Scatter'), ('SEMICIRCULARPROGRESSBARS', 'Semi-circular Progress bars'), ('VERTICALPROGRESSBARS', 'Vertical Progress bars'), ('WATERFALL', 'Waterfall'), ('DONUT', 'Donut'), ('GANTT', 'Gantt'), ('METER', 'Meter'), ('ODOMETER', 'Odometer'), ('RADIALSCATTER', 'Radial scatter'), ('THERMOMETER', 'Thermometer')], default='BAR', max_length=100, verbose_name='Type')),
                ('lg_width', models.PositiveSmallIntegerField(default=800, verbose_name='Large width')),
                ('lg_height', models.PositiveSmallIntegerField(default=400, verbose_name='Large height')),
                ('lg_max_width', models.PositiveSmallIntegerField(default=1200, verbose_name='Large max witdh')),
                ('lg_title_size', models.PositiveSmallIntegerField(default=18, verbose_name='Large title size')),
                ('lg_text_size', models.PositiveSmallIntegerField(default=14, verbose_name='Large text size')),
                ('lg_margin_inner', models.PositiveSmallIntegerField(default=25, verbose_name='Large margin inner')),
                ('md_width', models.PositiveSmallIntegerField(default=600, verbose_name='Medium width')),
                ('md_height', models.PositiveSmallIntegerField(default=300, verbose_name='Medium height')),
                ('md_max_width', models.PositiveSmallIntegerField(default=992, verbose_name='Medium max witdh')),
                ('md_title_size', models.PositiveSmallIntegerField(default=14, verbose_name='Medium title size')),
                ('md_text_size', models.PositiveSmallIntegerField(default=12, verbose_name='Medium text size')),
                ('md_margin_inner', models.PositiveSmallIntegerField(default=20, verbose_name='Medium margin inner')),
                ('sm_width', models.PositiveSmallIntegerField(default=400, verbose_name='Small width')),
                ('sm_height', models.PositiveSmallIntegerField(default=200, verbose_name='Small height')),
                ('sm_max_width', models.PositiveSmallIntegerField(default=768, verbose_name='Small max witdh')),
                ('sm_title_size', models.PositiveSmallIntegerField(default=12, verbose_name='Small title size')),
                ('sm_text_size', models.PositiveSmallIntegerField(default=10, verbose_name='Small text size')),
                ('sm_margin_inner', models.PositiveSmallIntegerField(default=10, verbose_name='Small margin inner')),
                ('options', mighty.models.JSONField(blank=True, null=True)),
                ('responsive_options', mighty.models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Graphic template',
                'verbose_name_plural': 'Graphic templates',
                'abstract': False,
                'default_permissions': ('add', 'detail', 'list', 'change', 'delete', 'disable', 'enable', 'export', 'import'),
            },
        ),
        migrations.CreateModel(
            name='Graphic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', mighty.models.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('title', models.CharField(max_length=255, verbose_name='Graphic title')),
                ('is_responsive', models.BooleanField(default=False, verbose_name='responsive')),
                ('svg_container', models.TextField(blank=True, null=True, verbose_name='Svg container HTML')),
                ('canvas_container', models.TextField(blank=True, null=True, verbose_name='Canvas container HTML')),
                ('width', models.PositiveSmallIntegerField(default=800, verbose_name='Width')),
                ('height', models.PositiveSmallIntegerField(default=400, verbose_name='Height')),
                ('max_width', models.PositiveSmallIntegerField(default=1200, verbose_name='Max witdh')),
                ('title_size', models.PositiveSmallIntegerField(default=18, verbose_name='Title size')),
                ('text_size', models.PositiveSmallIntegerField(default=14, verbose_name='Text size')),
                ('margin_inner', models.PositiveSmallIntegerField(default=25, verbose_name='Margin inner')),
                ('options', mighty.models.JSONField(blank=True, null=True)),
                ('responsive_options', mighty.models.JSONField(blank=True, null=True)),
                ('bar_values', mighty.models.JSONField(blank=True, null=True)),
                ('bipolar_values', mighty.models.JSONField(blank=True, null=True)),
                ('funnel_values', mighty.models.JSONField(blank=True, null=True)),
                ('gauge_values', mighty.models.JSONField(blank=True, null=True)),
                ('horizontalbar_values', mighty.models.JSONField(blank=True, null=True)),
                ('horizontalprogressbars_values', mighty.models.JSONField(blank=True, null=True)),
                ('line_values', mighty.models.JSONField(blank=True, null=True)),
                ('pie_values', mighty.models.JSONField(blank=True, null=True)),
                ('radar_values', mighty.models.JSONField(blank=True, null=True)),
                ('rose_values', mighty.models.JSONField(blank=True, null=True)),
                ('scatter_values', mighty.models.JSONField(blank=True, null=True)),
                ('semicircularprogressbars_values', mighty.models.JSONField(blank=True, null=True)),
                ('verticalprogressbars_values', mighty.models.JSONField(blank=True, null=True)),
                ('waterfall_values', mighty.models.JSONField(blank=True, null=True)),
                ('donut_values', mighty.models.JSONField(blank=True, null=True)),
                ('gantt_values', mighty.models.JSONField(blank=True, null=True)),
                ('meter_values', mighty.models.JSONField(blank=True, null=True)),
                ('odometer_values', mighty.models.JSONField(blank=True, null=True)),
                ('radialscatter_values', mighty.models.JSONField(blank=True, null=True)),
                ('thermometer_values', mighty.models.JSONField(blank=True, null=True)),
                ('templates', models.ManyToManyField(to='mighty.Template')),
            ],
            options={
                'verbose_name': 'Graphic',
                'verbose_name_plural': 'Graphics',
                'abstract': False,
                'default_permissions': ('add', 'detail', 'list', 'change', 'delete', 'disable', 'enable', 'export', 'import'),
            },
        ),
    ]
