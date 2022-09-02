import math
import os
import sys
from django.contrib.gis.gdal import GDALRaster
from django.contrib.gis.geos import Polygon
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand
from disasterinfosite.settings import BASE_DIR

# The width & height to tile rasters to.
# Empirically, tile sizes as large as 8053 work, while 10000 hits a memory overflow bug in either Django or GDAL and crashes.
# However, smaller tiles give us faster lookups, while really small (e.g. 10) make the data load interminably slow.
rasterTileSize = 128


######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadMappings
EQNisqually_2001_171004_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQTsunami_2022_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQLiquefaction_2019_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQCascadia_2020_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Volcano_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQSeattleNorth_2017_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood100yr500yr_2020_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Fire_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

LSHistorical_2020_220701_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

FloodSandbag_2016_220710_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Summer_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQUrm_2022_220710_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQTsunami_2022_220707_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Volcano_2016_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQCascadiaDisplaced_2017_220619_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

FloodDamInund_2013_220710_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

FloodCMZ_2015_220703_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Heat_2020_20220803_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

seattle_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Winter_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

LS_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}


FireHazardPotential_2020_220619_tif = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/reprojected/FireHazardPotential_2020_220619.tif'))
EQNisqually_2001_171004_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQNisqually_2001_171004.shp'))
Flood_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Flood_kingco.shp'))
EQTsunami_2022_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQTsunami_2022_220619.shp'))
EQLiquefaction_2019_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQLiquefaction_2019_220619.shp'))
EQCascadia_2020_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQCascadia_2020_220619.shp'))
Volcano_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Volcano_kingco.shp'))
LSSteepPotential_2018_220701_tif = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/reprojected/LSSteepPotential_2018_220701.tif'))
EQSeattleNorth_2017_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQSeattleNorth_2017_220619.shp'))
Flood100yr500yr_2020_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Flood100yr500yr_2020_220619.shp'))
FireWUI_2021_220619_tif = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/reprojected/FireWUI_2021_220619.tif'))
Fire_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Fire_kingco.shp'))
LSHistorical_2020_220701_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/LSHistorical_2020_220701.shp'))
FloodSandbag_2016_220710_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/FloodSandbag_2016_220710.shp'))
Summer_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Summer_kingco.shp'))
EQUrm_2022_220710_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQUrm_2022_220710.shp'))
EQTsunami_2022_220707_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQTsunami_2022_220707.shp'))
EQ_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQ_kingco.shp'))
Volcano_2016_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Volcano_2016_220619.shp'))
EQCascadiaDisplaced_2017_220619_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/EQCascadiaDisplaced_2017_220619.shp'))
FloodDamInund_2013_220710_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/FloodDamInund_2013_220710.shp'))
FloodCMZ_2015_220703_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/FloodCMZ_2015_220703.shp'))
Heat_2020_20220803_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Heat_2020_20220803.shp'))
seattle_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/seattle_kingco.shp'))
Winter_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Winter_kingco.shp'))
LS_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/LS_kingco.shp'))
# END OF GENERATED CODE BLOCK
######################################################

def tileLoadRaster(model, filename, band=0):
    tilesLoaded = 0
    tilesSkipped = 0
    model.objects.all().delete()
    sourceRaster = GDALRaster(filename, write=True)
    xTiles = math.ceil(sourceRaster.width / rasterTileSize)
    yTiles = math.ceil(sourceRaster.height / rasterTileSize)
    for x in range(0, xTiles):
        if x+1 != xTiles:
            width = rasterTileSize
        else:
            width = sourceRaster.width % rasterTileSize
        offsetX = x * rasterTileSize
        originX = sourceRaster.origin.x + offsetX * sourceRaster.scale.x
        for y in range(0, yTiles):
            if y+1 != yTiles:
                height = rasterTileSize
            else:
                height = sourceRaster.height % rasterTileSize
            offsetY = y * rasterTileSize
            originY = sourceRaster.origin.y + offsetY * sourceRaster.scale.y
            rasterTile = model(
                rast=GDALRaster({
                    'name': '/vsimem/tempraster',
                    'srid': sourceRaster.srid,
                    'width': width,
                    'height': height,
                    'origin': [originX, originY],
                    'scale': sourceRaster.scale,
                    'skew': sourceRaster.skew,
                    'bands': [{
                        'nodata_value': sourceRaster.bands[band].nodata_value,
                        'data': sourceRaster.bands[band].data(
                            offset=(offsetX, offsetY),
                            size=(width, height)
                        ),
                        'size': (width, height),
                        'offset': (0, 0)
                    }],
                    'datatype': 1  # GDT_Byte aka 8-bit unsigned integer
                })
            )
            if rasterTile.rast.bands[band].min is None:
                # This situation causes GDAL to print 2 lines of error code to the console, which are always safe to ignore, so we can use ANSI escape sequences to clean that up
                sys.stdout.write("\033[F\033[K")
                print("Skipping tile (" + str(x) + ", " + str(y) + ")\twith origin (" + str(originX)[:9] + ", " + str(originY)[
                      :9] + ")\tdue to lack of data. It's safe to ignore 'no valid pixels' GDAL_ERRORs in conjunction with this.")
                sys.stdout.write("\033[F\033[F\033[K")
                tilesSkipped += 1
            else:
                if y % 10 == 0:
                    sys.stdout.write('.')
                rasterTile.bbox = Polygon.from_bbox(rasterTile.rast.extent)
                rasterTile.save()
                tilesLoaded += 1
            sys.stdout.flush()  # flush often because otherwise the ANSI escape sequence "cleverness" becomes clumsiness when it goes out of sync
    print("\t...loaded", str(tilesLoaded), "tiles and skipped", str(
        tilesSkipped), "because they contained only NODATA pixels.")
    # clear remaining detritus from GDAL_ERRORs
    print("                                                                                          ")
    sys.stdout.write("\033[F\033[K")


def run(verbose=True):

    ######################################################
    # GENERATED CODE GOES HERE
    # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
    # loadGroups
    from disasterinfosite.models import ShapefileGroup
    fire = ShapefileGroup.objects.get_or_create(name='fire')
    quake = ShapefileGroup.objects.get_or_create(name='quake')
    flood = ShapefileGroup.objects.get_or_create(name='flood')
    volcano = ShapefileGroup.objects.get_or_create(name='volcano')
    slide = ShapefileGroup.objects.get_or_create(name='slide')
    summer = ShapefileGroup.objects.get_or_create(name='summer')
    winter = ShapefileGroup.objects.get_or_create(name='winter')
    # END OF GENERATED CODE BLOCK
    ######################################################

    ######################################################
    # GENERATED CODE GOES HERE
    # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
    # loadImports
    print('Loading data for FireHazardPotential_2020_220619')
    from disasterinfosite.models import FireHazardPotential_2020_220619
    tileLoadRaster(FireHazardPotential_2020_220619, FireHazardPotential_2020_220619_tif)

    print('Loading data for EQNisqually_2001_171004')
    from disasterinfosite.models import EQNisqually_2001_171004
    lm_EQNisqually_2001_171004 = LayerMapping(EQNisqually_2001_171004, EQNisqually_2001_171004_shp, EQNisqually_2001_171004_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQNisqually_2001_171004.save()

    print('Loading data for Flood_kingco')
    from disasterinfosite.models import Flood_kingco
    lm_Flood_kingco = LayerMapping(Flood_kingco, Flood_kingco_shp, Flood_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_kingco.save()

    print('Loading data for EQTsunami_2022_220619')
    from disasterinfosite.models import EQTsunami_2022_220619
    lm_EQTsunami_2022_220619 = LayerMapping(EQTsunami_2022_220619, EQTsunami_2022_220619_shp, EQTsunami_2022_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQTsunami_2022_220619.save()

    print('Loading data for EQLiquefaction_2019_220619')
    from disasterinfosite.models import EQLiquefaction_2019_220619
    lm_EQLiquefaction_2019_220619 = LayerMapping(EQLiquefaction_2019_220619, EQLiquefaction_2019_220619_shp, EQLiquefaction_2019_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQLiquefaction_2019_220619.save()

    print('Loading data for EQCascadia_2020_220619')
    from disasterinfosite.models import EQCascadia_2020_220619
    lm_EQCascadia_2020_220619 = LayerMapping(EQCascadia_2020_220619, EQCascadia_2020_220619_shp, EQCascadia_2020_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQCascadia_2020_220619.save()

    print('Loading data for Volcano_kingco')
    from disasterinfosite.models import Volcano_kingco
    lm_Volcano_kingco = LayerMapping(Volcano_kingco, Volcano_kingco_shp, Volcano_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Volcano_kingco.save()

    print('Loading data for LSSteepPotential_2018_220701')
    from disasterinfosite.models import LSSteepPotential_2018_220701
    tileLoadRaster(LSSteepPotential_2018_220701, LSSteepPotential_2018_220701_tif)

    print('Loading data for EQSeattleNorth_2017_220619')
    from disasterinfosite.models import EQSeattleNorth_2017_220619
    lm_EQSeattleNorth_2017_220619 = LayerMapping(EQSeattleNorth_2017_220619, EQSeattleNorth_2017_220619_shp, EQSeattleNorth_2017_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQSeattleNorth_2017_220619.save()

    print('Loading data for Flood100yr500yr_2020_220619')
    from disasterinfosite.models import Flood100yr500yr_2020_220619
    lm_Flood100yr500yr_2020_220619 = LayerMapping(Flood100yr500yr_2020_220619, Flood100yr500yr_2020_220619_shp, Flood100yr500yr_2020_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood100yr500yr_2020_220619.save()

    print('Loading data for FireWUI_2021_220619')
    from disasterinfosite.models import FireWUI_2021_220619
    tileLoadRaster(FireWUI_2021_220619, FireWUI_2021_220619_tif)

    print('Loading data for Fire_kingco')
    from disasterinfosite.models import Fire_kingco
    lm_Fire_kingco = LayerMapping(Fire_kingco, Fire_kingco_shp, Fire_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Fire_kingco.save()

    print('Loading data for LSHistorical_2020_220701')
    from disasterinfosite.models import LSHistorical_2020_220701
    lm_LSHistorical_2020_220701 = LayerMapping(LSHistorical_2020_220701, LSHistorical_2020_220701_shp, LSHistorical_2020_220701_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_LSHistorical_2020_220701.save()

    print('Loading data for FloodSandbag_2016_220710')
    from disasterinfosite.models import FloodSandbag_2016_220710
    lm_FloodSandbag_2016_220710 = LayerMapping(FloodSandbag_2016_220710, FloodSandbag_2016_220710_shp, FloodSandbag_2016_220710_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_FloodSandbag_2016_220710.save()

    print('Loading data for Summer_kingco')
    from disasterinfosite.models import Summer_kingco
    lm_Summer_kingco = LayerMapping(Summer_kingco, Summer_kingco_shp, Summer_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Summer_kingco.save()

    print('Loading data for EQUrm_2022_220710')
    from disasterinfosite.models import EQUrm_2022_220710
    lm_EQUrm_2022_220710 = LayerMapping(EQUrm_2022_220710, EQUrm_2022_220710_shp, EQUrm_2022_220710_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQUrm_2022_220710.save()

    print('Loading data for EQTsunami_2022_220707')
    from disasterinfosite.models import EQTsunami_2022_220707
    lm_EQTsunami_2022_220707 = LayerMapping(EQTsunami_2022_220707, EQTsunami_2022_220707_shp, EQTsunami_2022_220707_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQTsunami_2022_220707.save()

    print('Loading data for EQ_kingco')
    from disasterinfosite.models import EQ_kingco
    lm_EQ_kingco = LayerMapping(EQ_kingco, EQ_kingco_shp, EQ_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_kingco.save()

    print('Loading data for Volcano_2016_220619')
    from disasterinfosite.models import Volcano_2016_220619
    lm_Volcano_2016_220619 = LayerMapping(Volcano_2016_220619, Volcano_2016_220619_shp, Volcano_2016_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Volcano_2016_220619.save()

    print('Loading data for EQCascadiaDisplaced_2017_220619')
    from disasterinfosite.models import EQCascadiaDisplaced_2017_220619
    lm_EQCascadiaDisplaced_2017_220619 = LayerMapping(EQCascadiaDisplaced_2017_220619, EQCascadiaDisplaced_2017_220619_shp, EQCascadiaDisplaced_2017_220619_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQCascadiaDisplaced_2017_220619.save()

    print('Loading data for FloodDamInund_2013_220710')
    from disasterinfosite.models import FloodDamInund_2013_220710
    lm_FloodDamInund_2013_220710 = LayerMapping(FloodDamInund_2013_220710, FloodDamInund_2013_220710_shp, FloodDamInund_2013_220710_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_FloodDamInund_2013_220710.save()

    print('Loading data for FloodCMZ_2015_220703')
    from disasterinfosite.models import FloodCMZ_2015_220703
    lm_FloodCMZ_2015_220703 = LayerMapping(FloodCMZ_2015_220703, FloodCMZ_2015_220703_shp, FloodCMZ_2015_220703_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_FloodCMZ_2015_220703.save()

    print('Loading data for Heat_2020_20220803')
    from disasterinfosite.models import Heat_2020_20220803
    lm_Heat_2020_20220803 = LayerMapping(Heat_2020_20220803, Heat_2020_20220803_shp, Heat_2020_20220803_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Heat_2020_20220803.save()

    print('Loading data for seattle_kingco')
    from disasterinfosite.models import seattle_kingco
    lm_seattle_kingco = LayerMapping(seattle_kingco, seattle_kingco_shp, seattle_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_seattle_kingco.save()

    print('Loading data for Winter_kingco')
    from disasterinfosite.models import Winter_kingco
    lm_Winter_kingco = LayerMapping(Winter_kingco, Winter_kingco_shp, Winter_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Winter_kingco.save()

    print('Loading data for LS_kingco')
    from disasterinfosite.models import LS_kingco
    lm_LS_kingco = LayerMapping(LS_kingco, LS_kingco_shp, LS_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_LS_kingco.save()

    # END OF GENERATED CODE BLOCK
    ######################################################

    print("Data load finished.  GDAL_ERROR 'Failed to compute statistics, no valid pixels found in sampling' is safe to ignore if the data includes any raster files with any NODATA pixels.")


class Command(BaseCommand):
    help = """ Load data from the data directory """

    def handle(self, *args, **options):
        run()
