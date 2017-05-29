# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-29 23:29
from __future__ import unicode_literals

import disasterinfosite.models
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0004_model-translation'),
    ]

    operations = [
        migrations.CreateModel(
            name='LSLD_steepgradezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_steepgradezone.getGroup, on_delete=django.db.models.deletion.CASCADE, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.AlterField(
            model_name='eq_cascadia_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eq_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eq_liquefact_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eq_seattlefault72_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fire_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fire_wui_kingco_only',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flood_cmz_kingco',
            name='lookup_val',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flood_daminundation',
            name='lookup_val',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flood_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flood_nearest_sand_distr',
            name='lookup_val',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lsld_existing_features',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lsld_existingareas_kingco',
            name='lookup_val',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lsld_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='summer_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='volcano_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='volcano_lahar_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='winter_kingco',
            name='lookup_val',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_steepgradezone_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.LSLD_steepgradezone'),
        ),
    ]
