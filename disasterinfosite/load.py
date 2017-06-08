import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import GDALRaster


######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadMappings
LSLD_steepgradezone_mapping = {
    'bands[0]': 'bands[0]',
    'rast': GDALRaster('disasterinfosite/data/LSLD_steepgradezone.tif'
}

Summer_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Volcano_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Volcano_Lahar_kingco_mapping = {
    'lookup_val': 'Lookup_val',
    'geom': 'MULTIPOLYGON'
}

Winter_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}


LSLD_steepgradezone_rst = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/LSLD_steepgradezone.tif'))
Summer_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Summer_kingco.shp'))
Volcano_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Volcano_kingco.shp'))
Volcano_Lahar_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Volcano_Lahar_kingco.shp'))
Winter_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Winter_kingco.shp'))
# END OF GENERATED CODE BLOCK
######################################################


def run(verbose=True):

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadGroups
    from .models import ShapefileGroup
    quake = ShapefileGroup.objects.get_or_create(name='quake')
    summer = ShapefileGroup.objects.get_or_create(name='summer')
    volcano = ShapefileGroup.objects.get_or_create(name='volcano')
    winter = ShapefileGroup.objects.get_or_create(name='winter')
# END OF GENERATED CODE BLOCK
######################################################

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadImports
    from .models import LSLD_steepgradezone
    lm_LSLD_steepgradezone = LayerMapping(LSLD_steepgradezone, LSLD_steepgradezone_shp, LSLD_steepgradezone_mapping, transform=True, encoding='UTF-8', unique=['bands[0]'])
    lm_LSLD_steepgradezone.save(strict=True, verbose=verbose)

    from .models import Summer_kingco
    lm_Summer_kingco = LayerMapping(Summer_kingco, Summer_kingco_shp, Summer_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Summer_kingco.save(strict=True, verbose=verbose)

    from .models import Volcano_kingco
    lm_Volcano_kingco = LayerMapping(Volcano_kingco, Volcano_kingco_shp, Volcano_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Volcano_kingco.save(strict=True, verbose=verbose)

    from .models import Volcano_Lahar_kingco
    lm_Volcano_Lahar_kingco = LayerMapping(Volcano_Lahar_kingco, Volcano_Lahar_kingco_shp, Volcano_Lahar_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Volcano_Lahar_kingco.save(strict=True, verbose=verbose)

    from .models import Winter_kingco
    lm_Winter_kingco = LayerMapping(Winter_kingco, Winter_kingco_shp, Winter_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Winter_kingco.save(strict=True, verbose=verbose)

# END OF GENERATED CODE BLOCK
######################################################

