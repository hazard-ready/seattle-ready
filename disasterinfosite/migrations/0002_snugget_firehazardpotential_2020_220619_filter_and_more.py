# Generated by Django 4.0.7 on 2022-09-28 00:36

import disasterinfosite.models
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snugget',
            name='FireHazardPotential_2020_220619_filter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='FireWUI_2021_220619_filter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSSteepPotential_2018_220701_filter',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Winter_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Winter_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Volcano_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Volcano_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Volcano_2016_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Volcano_2016_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Summer_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Summer_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='seattle_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.seattle_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='LSSteepPotential_2018_220701',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
                ('bbox', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSSteepPotential_2018_220701.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='LSHistorical_2020_220701',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSHistorical_2020_220701.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='LS_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LS_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Heat_2020_20220803',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Heat_2020_20220803.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='FloodSandbag_2016_220710',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.FloodSandbag_2016_220710.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='FloodDamInund_2013_220710',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.FloodDamInund_2013_220710.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='FloodCMZ_2015_220703',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.FloodCMZ_2015_220703.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood100yr500yr_2020_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood100yr500yr_2020_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='FireWUI_2021_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
                ('bbox', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.FireWUI_2021_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='FireHazardPotential_2020_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rast', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
                ('bbox', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.FireHazardPotential_2020_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Fire_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Fire_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQUrm_2022_220710',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQUrm_2022_220710.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQTsunami_2022_220707',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQTsunami_2022_220707.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQTsunami_2022_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQTsunami_2022_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQSeattleNorth_2017_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQSeattleNorth_2017_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQNisqually_2001_171004',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQNisqually_2001_171004.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQLiquefaction_2019_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQLiquefaction_2019_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQCascadiaDisplaced_2017_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQCascadiaDisplaced_2017_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQCascadia_2020_220619',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQCascadia_2020_220619.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQ_kingco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_kingco.getGroup, on_delete=django.db.models.deletion.PROTECT, to='disasterinfosite.shapefilegroup')),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQCascadiaDisplaced_2017_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqcascadiadisplaced_2017_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQCascadia_2020_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqcascadia_2020_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQLiquefaction_2019_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqliquefaction_2019_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQNisqually_2001_171004_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqnisqually_2001_171004'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQSeattleNorth_2017_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqseattlenorth_2017_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQTsunami_2022_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqtsunami_2022_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQTsunami_2022_220707_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eqtsunami_2022_220707'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQUrm_2022_220710_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.equrm_2022_220710'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.eq_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.fire_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood100yr500yr_2020_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.flood100yr500yr_2020_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='FloodCMZ_2015_220703_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.floodcmz_2015_220703'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='FloodDamInund_2013_220710_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.flooddaminund_2013_220710'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='FloodSandbag_2016_220710_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.floodsandbag_2016_220710'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.flood_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Heat_2020_20220803_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.heat_2020_20220803'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSHistorical_2020_220701_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.lshistorical_2020_220701'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LS_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.ls_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Summer_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.summer_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Volcano_2016_220619_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.volcano_2016_220619'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Volcano_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.volcano_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Winter_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.winter_kingco'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='seattle_kingco_filter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.seattle_kingco'),
        ),
    ]
