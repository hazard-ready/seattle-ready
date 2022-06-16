# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import disasterinfosite.models
import django.db.models.deletion
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQ_Liquefact_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_Liquefact_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Nisqual68_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_Nisqual68_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_SeattleFault72_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_SeattleFault72_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Tsunami_SeaFault72_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_Tsunami_SeaFault72_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_URM_DensityZones_seattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_URM_DensityZones_seattle.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_WUI_kingco_only',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Fire_WUI_kingco_only.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_100yr_wUrban_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_100yr_wUrban_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_500yr_wUrban_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_500yr_wUrban_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_CMZ_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_CMZ_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_DamInundation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_DamInundation.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_nearest_sand_distr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_nearest_sand_distr.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Hubs_Nearest_seattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Hubs_Nearest_seattle.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_ExistingAreas_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_ExistingAreas_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_Prone_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_Prone_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Volcano_Lahar_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Volcano_Lahar_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Cascadia_kingco',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE, default=disasterinfosite.models.EQ_Cascadia_kingco.getGroup)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Cascadia_kingco_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.EQ_Cascadia_kingco', blank=True, related_name='+', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Liquefact_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_Liquefact_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Nisqual68_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_Nisqual68_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_SeattleFault72_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_SeattleFault72_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Tsunami_SeaFault72_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_Tsunami_SeaFault72_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_URM_DensityZones_seattle_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_URM_DensityZones_seattle', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_WUI_kingco_only_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Fire_WUI_kingco_only', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_100yr_wUrban_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_100yr_wUrban_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_500yr_wUrban_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_500yr_wUrban_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_CMZ_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_CMZ_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_DamInundation_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_DamInundation', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_nearest_sand_distr_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_nearest_sand_distr', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Hubs_Nearest_seattle_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Hubs_Nearest_seattle', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_ExistingAreas_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.LSLD_ExistingAreas_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_Prone_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.LSLD_Prone_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Volcano_Lahar_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Volcano_Lahar_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.CreateModel(
            name='EQ_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Volcano_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Volcano_kingco.getGroup, to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_kingco_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.EQ_kingco', related_name='+', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_kingco_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.Flood_kingco', related_name='+', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_kingco_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.LSLD_kingco', related_name='+', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Volcano_kingco_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.Volcano_kingco', related_name='+', blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Fire_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE, default=disasterinfosite.models.Fire_kingco.getGroup)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_kingco_filter',
            field=models.ForeignKey(null=True, blank=True, to='disasterinfosite.Fire_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
                migrations.CreateModel(
            name='LSLD_existing_features',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE, default=disasterinfosite.models.LSLD_existing_features.getGroup)),
            ],
        ),
        migrations.CreateModel(
            name='Summer_kingco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE, default=disasterinfosite.models.Summer_kingco.getGroup)),
            ],
        ),
        migrations.CreateModel(
            name='Winter_kingco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', on_delete=django.db.models.deletion.CASCADE, default=disasterinfosite.models.Winter_kingco.getGroup)),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_steepgradezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gridcode', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_steepgradezone.getGroup, on_delete=django.db.models.deletion.CASCADE, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_existing_features_filter',
            field=models.ForeignKey(to='disasterinfosite.LSLD_existing_features', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Summer_kingco_filter',
            field=models.ForeignKey(to='disasterinfosite.Summer_kingco', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Winter_kingco_filter',
            field=models.ForeignKey(to='disasterinfosite.Winter_kingco', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_steepgradezone_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.LSLD_steepgradezone'),
        ),
    ]
