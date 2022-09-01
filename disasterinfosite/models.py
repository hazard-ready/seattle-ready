from collections import OrderedDict
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import Extent
from embed_video.fields import EmbedVideoField
from model_utils.managers import InheritanceManager
from solo.models import SingletonModel
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator


SNUG_TEXT = 0
SNUG_VIDEO = 1
SNUG_SLIDESHOW = 2

SNUGGET_TYPES = (
    ('SNUG_TEXT', 'TextSnugget'),
    ('SNUG_VIDEO', 'EmbedSnugget'),
    ('SNUG_SLIDESHOW', 'SlideshowSnugget')
)


class PreparednessAction(models.Model):
    title = models.TextField(default="")
    image = models.ImageField(upload_to="prepare_images")
    cost = models.IntegerField(default=0,
                               validators=[
                                   RangeMinValueValidator(0),
                                   RangeMaxValueValidator(4)
                               ])
    happy_text = models.TextField(default="")
    useful_text = models.TextField(default="")
    property_text = models.TextField(default="")
    content_text = models.TextField(default="")
    link_text = models.TextField(default="")
    link_icon = models.ImageField(upload_to="prepare_images")
    link = models.URLField(default="")
    slug = models.TextField(default="")

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    """ A model representing a user's information that isn't their username, password, or email address """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)
    actions_taken = models.ManyToManyField(PreparednessAction, blank=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return "{0}: {1}, {2} {3}, {4} {5}: {6}".format(self.user, self.address1, self.address2, self.city, self.state, self.zip_code, self.actions_taken.all().values_list('title', flat=True))


class SiteSettings(SingletonModel):
    """A singleton model to represent site-wide settings."""
    area_name = models.CharField(
        max_length=100,
        default="the affected area",
        help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'."
    )
    about_text = models.TextField(
        default="Information about your organization goes here.",
        help_text="Describe the data and the agencies that it came from."
    )
    contact_email = models.EmailField(
        blank=True,
        help_text="Put a contact email for the maintainer of this site here."
    )
    site_url = models.URLField(
        default="https://www.example.com",
        help_text="Put the URL to this site here."
    )
    site_title = models.CharField(
        max_length=50,
        default="Your Title Here!"
    )
    site_description = models.CharField(
        max_length=200,
        default="A disaster preparedness website",
        help_text="A small, catchy description for this site."
    )
    intro_text = models.TextField(
        default="A natural disaster could strike your area at any time.",
        help_text="A description of what we are trying to help people prepare for, or the goal of your site."
    )
    who_made_this = models.TextField(
        default="Information about the creators and maintainers of this particular site.",
        help_text="Include information about who you are and how to contact you."
    )
    data_download = models.URLField(
        blank=True,
        help_text="A link where people can download a zipfile of all the data that powers this site."
    )

    def __unicode__(self):
        return u"Site Settings"

    class Meta:
        verbose_name = "Site Settings"


class Location(SingletonModel):
    """A singleton model to represent the location covered by this website's data"""

    def __unicode__(self):
        return u"Location Information"

    @staticmethod
    def get_data_bounds():
        bounds = {
            ######################################################
            # GENERATED CODE GOES HERE
            # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
            # locationsList
            'FireHazardPotential_2020_220619': FireHazardPotential_2020_220619.objects.data_bounds(),
            'EQNisqually_2001_171004': EQNisqually_2001_171004.objects.data_bounds(),
            'Flood_kingco': Flood_kingco.objects.data_bounds(),
            'EQTsunami_2022_220619': EQTsunami_2022_220619.objects.data_bounds(),
            'EQLiquefaction_2019_220619': EQLiquefaction_2019_220619.objects.data_bounds(),
            'EQCascadia_2020_220619': EQCascadia_2020_220619.objects.data_bounds(),
            'seattle_districts': seattle_districts.objects.data_bounds(),
            'Volcano_kingco': Volcano_kingco.objects.data_bounds(),
            'LSSteepPotential_2018_220701': LSSteepPotential_2018_220701.objects.data_bounds(),
            'EQSeattleNorth_2017_220619': EQSeattleNorth_2017_220619.objects.data_bounds(),
            'seattle': seattle.objects.data_bounds(),
            'Flood100yr500yr_2020_220619': Flood100yr500yr_2020_220619.objects.data_bounds(),
            'FireWUI_2021_220619': FireWUI_2021_220619.objects.data_bounds(),
            'Fire_kingco': Fire_kingco.objects.data_bounds(),
            'LSHistorical_2020_220701': LSHistorical_2020_220701.objects.data_bounds(),
            'FloodSandbag_2016_220710': FloodSandbag_2016_220710.objects.data_bounds(),
            'Summer_kingco': Summer_kingco.objects.data_bounds(),
            'EQUrm_2022_220710': EQUrm_2022_220710.objects.data_bounds(),
            'EQTsunami_2022_220707': EQTsunami_2022_220707.objects.data_bounds(),
            'EQ_kingco': EQ_kingco.objects.data_bounds(),
            'Volcano_2016_220619': Volcano_2016_220619.objects.data_bounds(),
            'EQCascadiaDisplaced_2017_220619': EQCascadiaDisplaced_2017_220619.objects.data_bounds(),
            'kingco_water': kingco_water.objects.data_bounds(),
            'FloodDamInund_2013_220710': FloodDamInund_2013_220710.objects.data_bounds(),
            'kingco_roads': kingco_roads.objects.data_bounds(),
            'FloodCMZ_2015_220703': FloodCMZ_2015_220703.objects.data_bounds(),
            'kingco_cities': kingco_cities.objects.data_bounds(),
            'Heat_2020_20220803': Heat_2020_20220803.objects.data_bounds(),
            'poly': poly.objects.data_bounds(),
            'poly_mask': poly_mask.objects.data_bounds(),
            'seattle_kingco': seattle_kingco.objects.data_bounds(),
            'kingco': kingco.objects.data_bounds(),
            'Winter_kingco': Winter_kingco.objects.data_bounds(),
            'LS_kingco': LS_kingco.objects.data_bounds()
            # END OF GENERATED CODE BLOCK
            ######################################################
        }

        # The smallest/largest possible values, as appropriate, so the map will display
        # something if there is no data
        north = [-80]
        west = [180]
        south = [80]
        east = [-180]

        for box in bounds.values():
            if box is not None:
                west.append(box[0])
                south.append(box[1])
                east.append(box[2])
                north.append(box[3])

        # The largest box that contains all the bounding boxes, how Leaflet wants it.
        return [[min(south), min(west)], [max(north), max(east)]]

    class Meta:
        verbose_name = "Location Information"


class ShapeManager(models.Manager):
    def data_bounds(self):
        return self.aggregate(Extent('geom'))['geom__extent']


class RasterManager(models.Manager):
    def data_bounds(self):
        return self.aggregate(Extent('bbox'))['bbox__extent']


class ShapefileGroup(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, default="")
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order, from top to bottom, in which you would like this group to appear, when applicable."
    )
    note = models.TextField(
        blank=True, help_text='A note that appears above all snuggets in this section. Use for data caveats or warnings.')

    def __str__(self):
        return self.name

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsClasses
class FireHazardPotential_2020_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='fire')[0]

    rast = models.RasterField(srid=4326)
    bbox = models.PolygonField(srid=4326)
    objects = RasterManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.rast.name) + ',	' + str(self.bbox) 

class EQNisqually_2001_171004(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class Flood_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='flood')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQTsunami_2022_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQLiquefaction_2019_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQCascadia_2020_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class seattle_districts(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    objectid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.objectid)

class Volcano_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='volcano')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class LSSteepPotential_2018_220701(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='slide')[0]

    rast = models.RasterField(srid=4326)
    bbox = models.PolygonField(srid=4326)
    objects = RasterManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.rast.name) + ',	' + str(self.bbox) 

class EQSeattleNorth_2017_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class seattle(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    objectid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.objectid)

class Flood100yr500yr_2020_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='flood')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class FireWUI_2021_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='fire')[0]

    rast = models.RasterField(srid=4326)
    bbox = models.PolygonField(srid=4326)
    objects = RasterManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.rast.name) + ',	' + str(self.bbox) 

class Fire_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='fire')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class LSHistorical_2020_220701(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='slide')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class FloodSandbag_2016_220710(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='flood')[0]

    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class Summer_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='summer')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQUrm_2022_220710(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQTsunami_2022_220707(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQ_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class Volcano_2016_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='volcano')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class EQCascadiaDisplaced_2017_220619(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class kingco_water(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='flood')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class FloodDamInund_2013_220710(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='flood')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class kingco_roads(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    number = models.CharField(max_length=80)
    geom = models.MultiLineStringField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.number)

class FloodCMZ_2015_220703(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='flood')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class kingco_cities(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    objectid = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.objectid)

class Heat_2020_20220803(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='summer')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class poly(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    shape_id = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.shape_id)

class poly_mask(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class seattle_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class Winter_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='winter')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

class LS_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='slide')[0]

    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.lookup_val)

# END OF GENERATED CODE BLOCK
######################################################


class SnuggetType(models.Model):
    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=255, choices=SNUGGET_TYPES)

    def __str__(self):
        return self.name


class SnuggetSection(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(
        max_length=50, help_text="The name to show for this section", default="")
    collapsible = models.BooleanField(
        default=True, help_text='Whether this section of the data is collapsible')
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order in which you'd like this to appear in the tab. 0 is at the top."
    )

    def __str__(self):
        return self.name


class SnuggetPopOut(models.Model):
    text = models.TextField(default='')
    image = models.ImageField(upload_to="popout_images")
    link = models.TextField(default='', max_length=255)
    alt_text = models.TextField(default='', max_length=255)
    video = EmbedVideoField(null=True)

    @property
    def has_content(self):
        "Returns true if this popout has some content"
        return (self.text or self.image or self.link or self.video)

    def __str__(self):
        return self.text[:100]


@receiver(pre_save, sender=SnuggetSection)
@receiver(pre_save, sender=ShapefileGroup)
def default_display_name(sender, instance, *args, **kwargs):
    if not instance.display_name:
        instance.display_name = instance.name


# looks up a point in a set of rasters and returns the first non-NODATA value it finds
# or None if there are no rasters, the point is not within any of them or it's in a NODATA pixel.
# raster algebra taken from the django-raster project version 0.6 at
# https://github.com/geodesign/django-raster/blob/master/raster/utils.py
def rasterPointLookup(rasterCollection, lng, lat, band=0):
    # if we have no data at all, then save time and return None immediately
    sampleBBOX = rasterCollection.objects.only("bbox").first().bbox
    if sampleBBOX is None:
        return None

    rasterPoint = OGRGeometry(
        'POINT({0} {1})'.format(lng, lat), srs=sampleBBOX.srs)
    vectorPoint = Point(lng, lat, srid=sampleBBOX.srid)

    # Using the filter here lets PostGIS do an indexed search on the bbox field, which is much faster than stepping through the objects.
    # Note that it will almost always only return one raster, but there could theoretically be 2 or 4 if our point is perfectly on a tile boundary.
    # In that instance, we return the first non-NODATA value we find.
    for tile in rasterCollection.objects.filter(bbox__contains=vectorPoint).all():
        # only bother to check for data if we're within the bounds
        rst = tile.rast
        offset = (abs(
            rst.origin.x - rasterPoint.coords[0]), abs(rst.origin.y - rasterPoint.coords[1]))
        offset_idx = [int(offset[0] / abs(rst.scale.x)),
                      int(offset[1] / abs(rst.scale.y))]

        # points very close to the boundary can get rounded to 1 pixel beyond it, so fix that here
        if offset_idx[0] == rst.width:
            offset_idx[0] -= 1
        if offset_idx[1] == rst.height:
            offset_idx[1] -= 1

        result = rst.bands[band].data(offset=offset_idx, size=(1, 1))[0]
        if result != rst.bands[band].nodata_value:
            return rst.bands[band].data(offset=offset_idx, size=(1, 1))[0]

    return None


class Snugget(models.Model):
    objects = InheritanceManager()

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsFilters
    FireHazardPotential_2020_220619_filter = models.IntegerField(null=True)
    EQNisqually_2001_171004_filter = models.ForeignKey(EQNisqually_2001_171004, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Flood_kingco_filter = models.ForeignKey(Flood_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQTsunami_2022_220619_filter = models.ForeignKey(EQTsunami_2022_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQLiquefaction_2019_220619_filter = models.ForeignKey(EQLiquefaction_2019_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQCascadia_2020_220619_filter = models.ForeignKey(EQCascadia_2020_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    seattle_districts_filter = models.ForeignKey(seattle_districts, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Volcano_kingco_filter = models.ForeignKey(Volcano_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    LSSteepPotential_2018_220701_filter = models.IntegerField(null=True)
    EQSeattleNorth_2017_220619_filter = models.ForeignKey(EQSeattleNorth_2017_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    seattle_filter = models.ForeignKey(seattle, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Flood100yr500yr_2020_220619_filter = models.ForeignKey(Flood100yr500yr_2020_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    FireWUI_2021_220619_filter = models.IntegerField(null=True)
    Fire_kingco_filter = models.ForeignKey(Fire_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    LSHistorical_2020_220701_filter = models.ForeignKey(LSHistorical_2020_220701, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    FloodSandbag_2016_220710_filter = models.ForeignKey(FloodSandbag_2016_220710, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Summer_kingco_filter = models.ForeignKey(Summer_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQUrm_2022_220710_filter = models.ForeignKey(EQUrm_2022_220710, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQTsunami_2022_220707_filter = models.ForeignKey(EQTsunami_2022_220707, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQ_kingco_filter = models.ForeignKey(EQ_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Volcano_2016_220619_filter = models.ForeignKey(Volcano_2016_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQCascadiaDisplaced_2017_220619_filter = models.ForeignKey(EQCascadiaDisplaced_2017_220619, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    kingco_water_filter = models.ForeignKey(kingco_water, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    FloodDamInund_2013_220710_filter = models.ForeignKey(FloodDamInund_2013_220710, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    kingco_roads_filter = models.ForeignKey(kingco_roads, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    FloodCMZ_2015_220703_filter = models.ForeignKey(FloodCMZ_2015_220703, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    kingco_cities_filter = models.ForeignKey(kingco_cities, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Heat_2020_20220803_filter = models.ForeignKey(Heat_2020_20220803, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    poly_filter = models.ForeignKey(poly, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    poly_mask_filter = models.ForeignKey(poly_mask, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    seattle_kingco_filter = models.ForeignKey(seattle_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    kingco_filter = models.ForeignKey(kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Winter_kingco_filter = models.ForeignKey(Winter_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    LS_kingco_filter = models.ForeignKey(LS_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
# END OF GENERATED CODE BLOCK
######################################################

    section = models.ForeignKey(
        SnuggetSection, related_name='+', on_delete=models.PROTECT)
    group = models.ForeignKey(
        ShapefileGroup, on_delete=models.PROTECT, null=True)
    pop_out = models.OneToOneField(
        SnuggetPopOut, on_delete=models.PROTECT, blank=True, null=True)
    percentage = models.FloatField(null=True)
    order = models.IntegerField(default=0)

    def getRelatedTemplate(self):
        return "snugget.html"

    @staticmethod
    def findSnuggetsForPoint(lat=0, lng=0, merge_deform=True):
        pnt = Point(lng, lat)
        groups = ShapefileGroup.objects.all().order_by('order_of_appearance')
        groupsDict = OrderedDict({el: [] for el in groups})

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsGeoFilters
        FireHazardPotential_2020_220619_rating = rasterPointLookup(FireHazardPotential_2020_220619, lng, lat)
        if FireHazardPotential_2020_220619_rating is not None:
            FireHazardPotential_2020_220619_snugget = Snugget.objects.filter(FireHazardPotential_2020_220619_filter__exact=FireHazardPotential_2020_220619_rating).order_by('order').select_subclasses()
            if FireHazardPotential_2020_220619_snugget:
                groupsDict[FireHazardPotential_2020_220619.getGroup()].extend(FireHazardPotential_2020_220619_snugget)

        qs_EQNisqually_2001_171004 = EQNisqually_2001_171004.objects.filter(geom__contains=pnt)
        EQNisqually_2001_171004_rating = qs_EQNisqually_2001_171004.values_list('lookup_val', flat=True)
        for rating in EQNisqually_2001_171004_rating:
            EQNisqually_2001_171004_snugget = Snugget.objects.filter(EQNisqually_2001_171004_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQNisqually_2001_171004_snugget:
                groupsDict[EQNisqually_2001_171004.getGroup()].extend(EQNisqually_2001_171004_snugget)

        qs_Flood_kingco = Flood_kingco.objects.filter(geom__contains=pnt)
        Flood_kingco_rating = qs_Flood_kingco.values_list('lookup_val', flat=True)
        for rating in Flood_kingco_rating:
            Flood_kingco_snugget = Snugget.objects.filter(Flood_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Flood_kingco_snugget:
                groupsDict[Flood_kingco.getGroup()].extend(Flood_kingco_snugget)

        qs_EQTsunami_2022_220619 = EQTsunami_2022_220619.objects.filter(geom__contains=pnt)
        EQTsunami_2022_220619_rating = qs_EQTsunami_2022_220619.values_list('lookup_val', flat=True)
        for rating in EQTsunami_2022_220619_rating:
            EQTsunami_2022_220619_snugget = Snugget.objects.filter(EQTsunami_2022_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQTsunami_2022_220619_snugget:
                groupsDict[EQTsunami_2022_220619.getGroup()].extend(EQTsunami_2022_220619_snugget)

        qs_EQLiquefaction_2019_220619 = EQLiquefaction_2019_220619.objects.filter(geom__contains=pnt)
        EQLiquefaction_2019_220619_rating = qs_EQLiquefaction_2019_220619.values_list('lookup_val', flat=True)
        for rating in EQLiquefaction_2019_220619_rating:
            EQLiquefaction_2019_220619_snugget = Snugget.objects.filter(EQLiquefaction_2019_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQLiquefaction_2019_220619_snugget:
                groupsDict[EQLiquefaction_2019_220619.getGroup()].extend(EQLiquefaction_2019_220619_snugget)

        qs_EQCascadia_2020_220619 = EQCascadia_2020_220619.objects.filter(geom__contains=pnt)
        EQCascadia_2020_220619_rating = qs_EQCascadia_2020_220619.values_list('lookup_val', flat=True)
        for rating in EQCascadia_2020_220619_rating:
            EQCascadia_2020_220619_snugget = Snugget.objects.filter(EQCascadia_2020_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQCascadia_2020_220619_snugget:
                groupsDict[EQCascadia_2020_220619.getGroup()].extend(EQCascadia_2020_220619_snugget)

        qs_seattle_districts = seattle_districts.objects.filter(geom__contains=pnt)
        seattle_districts_rating = qs_seattle_districts.values_list('objectid', flat=True)
        for rating in seattle_districts_rating:
            seattle_districts_snugget = Snugget.objects.filter(seattle_districts_filter__objectid__exact=rating).order_by('order').select_subclasses()
            if seattle_districts_snugget:
                groupsDict[seattle_districts.getGroup()].extend(seattle_districts_snugget)

        qs_Volcano_kingco = Volcano_kingco.objects.filter(geom__contains=pnt)
        Volcano_kingco_rating = qs_Volcano_kingco.values_list('lookup_val', flat=True)
        for rating in Volcano_kingco_rating:
            Volcano_kingco_snugget = Snugget.objects.filter(Volcano_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Volcano_kingco_snugget:
                groupsDict[Volcano_kingco.getGroup()].extend(Volcano_kingco_snugget)

        LSSteepPotential_2018_220701_rating = rasterPointLookup(LSSteepPotential_2018_220701, lng, lat)
        if LSSteepPotential_2018_220701_rating is not None:
            LSSteepPotential_2018_220701_snugget = Snugget.objects.filter(LSSteepPotential_2018_220701_filter__exact=LSSteepPotential_2018_220701_rating).order_by('order').select_subclasses()
            if LSSteepPotential_2018_220701_snugget:
                groupsDict[LSSteepPotential_2018_220701.getGroup()].extend(LSSteepPotential_2018_220701_snugget)

        qs_EQSeattleNorth_2017_220619 = EQSeattleNorth_2017_220619.objects.filter(geom__contains=pnt)
        EQSeattleNorth_2017_220619_rating = qs_EQSeattleNorth_2017_220619.values_list('lookup_val', flat=True)
        for rating in EQSeattleNorth_2017_220619_rating:
            EQSeattleNorth_2017_220619_snugget = Snugget.objects.filter(EQSeattleNorth_2017_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQSeattleNorth_2017_220619_snugget:
                groupsDict[EQSeattleNorth_2017_220619.getGroup()].extend(EQSeattleNorth_2017_220619_snugget)

        qs_seattle = seattle.objects.filter(geom__contains=pnt)
        seattle_rating = qs_seattle.values_list('objectid', flat=True)
        for rating in seattle_rating:
            seattle_snugget = Snugget.objects.filter(seattle_filter__objectid__exact=rating).order_by('order').select_subclasses()
            if seattle_snugget:
                groupsDict[seattle.getGroup()].extend(seattle_snugget)

        qs_Flood100yr500yr_2020_220619 = Flood100yr500yr_2020_220619.objects.filter(geom__contains=pnt)
        Flood100yr500yr_2020_220619_rating = qs_Flood100yr500yr_2020_220619.values_list('lookup_val', flat=True)
        for rating in Flood100yr500yr_2020_220619_rating:
            Flood100yr500yr_2020_220619_snugget = Snugget.objects.filter(Flood100yr500yr_2020_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Flood100yr500yr_2020_220619_snugget:
                groupsDict[Flood100yr500yr_2020_220619.getGroup()].extend(Flood100yr500yr_2020_220619_snugget)

        FireWUI_2021_220619_rating = rasterPointLookup(FireWUI_2021_220619, lng, lat)
        if FireWUI_2021_220619_rating is not None:
            FireWUI_2021_220619_snugget = Snugget.objects.filter(FireWUI_2021_220619_filter__exact=FireWUI_2021_220619_rating).order_by('order').select_subclasses()
            if FireWUI_2021_220619_snugget:
                groupsDict[FireWUI_2021_220619.getGroup()].extend(FireWUI_2021_220619_snugget)

        qs_Fire_kingco = Fire_kingco.objects.filter(geom__contains=pnt)
        Fire_kingco_rating = qs_Fire_kingco.values_list('lookup_val', flat=True)
        for rating in Fire_kingco_rating:
            Fire_kingco_snugget = Snugget.objects.filter(Fire_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Fire_kingco_snugget:
                groupsDict[Fire_kingco.getGroup()].extend(Fire_kingco_snugget)

        qs_LSHistorical_2020_220701 = LSHistorical_2020_220701.objects.filter(geom__contains=pnt)
        LSHistorical_2020_220701_rating = qs_LSHistorical_2020_220701.values_list('lookup_val', flat=True)
        for rating in LSHistorical_2020_220701_rating:
            LSHistorical_2020_220701_snugget = Snugget.objects.filter(LSHistorical_2020_220701_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if LSHistorical_2020_220701_snugget:
                groupsDict[LSHistorical_2020_220701.getGroup()].extend(LSHistorical_2020_220701_snugget)

        qs_FloodSandbag_2016_220710 = FloodSandbag_2016_220710.objects.filter(geom__contains=pnt)
        FloodSandbag_2016_220710_rating = qs_FloodSandbag_2016_220710.values_list('lookup_val', flat=True)
        for rating in FloodSandbag_2016_220710_rating:
            FloodSandbag_2016_220710_snugget = Snugget.objects.filter(FloodSandbag_2016_220710_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if FloodSandbag_2016_220710_snugget:
                groupsDict[FloodSandbag_2016_220710.getGroup()].extend(FloodSandbag_2016_220710_snugget)

        qs_Summer_kingco = Summer_kingco.objects.filter(geom__contains=pnt)
        Summer_kingco_rating = qs_Summer_kingco.values_list('lookup_val', flat=True)
        for rating in Summer_kingco_rating:
            Summer_kingco_snugget = Snugget.objects.filter(Summer_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Summer_kingco_snugget:
                groupsDict[Summer_kingco.getGroup()].extend(Summer_kingco_snugget)

        qs_EQUrm_2022_220710 = EQUrm_2022_220710.objects.filter(geom__contains=pnt)
        EQUrm_2022_220710_rating = qs_EQUrm_2022_220710.values_list('lookup_val', flat=True)
        for rating in EQUrm_2022_220710_rating:
            EQUrm_2022_220710_snugget = Snugget.objects.filter(EQUrm_2022_220710_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQUrm_2022_220710_snugget:
                groupsDict[EQUrm_2022_220710.getGroup()].extend(EQUrm_2022_220710_snugget)

        qs_EQTsunami_2022_220707 = EQTsunami_2022_220707.objects.filter(geom__contains=pnt)
        EQTsunami_2022_220707_rating = qs_EQTsunami_2022_220707.values_list('lookup_val', flat=True)
        for rating in EQTsunami_2022_220707_rating:
            EQTsunami_2022_220707_snugget = Snugget.objects.filter(EQTsunami_2022_220707_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQTsunami_2022_220707_snugget:
                groupsDict[EQTsunami_2022_220707.getGroup()].extend(EQTsunami_2022_220707_snugget)

        qs_EQ_kingco = EQ_kingco.objects.filter(geom__contains=pnt)
        EQ_kingco_rating = qs_EQ_kingco.values_list('lookup_val', flat=True)
        for rating in EQ_kingco_rating:
            EQ_kingco_snugget = Snugget.objects.filter(EQ_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQ_kingco_snugget:
                groupsDict[EQ_kingco.getGroup()].extend(EQ_kingco_snugget)

        qs_Volcano_2016_220619 = Volcano_2016_220619.objects.filter(geom__contains=pnt)
        Volcano_2016_220619_rating = qs_Volcano_2016_220619.values_list('lookup_val', flat=True)
        for rating in Volcano_2016_220619_rating:
            Volcano_2016_220619_snugget = Snugget.objects.filter(Volcano_2016_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Volcano_2016_220619_snugget:
                groupsDict[Volcano_2016_220619.getGroup()].extend(Volcano_2016_220619_snugget)

        qs_EQCascadiaDisplaced_2017_220619 = EQCascadiaDisplaced_2017_220619.objects.filter(geom__contains=pnt)
        EQCascadiaDisplaced_2017_220619_rating = qs_EQCascadiaDisplaced_2017_220619.values_list('lookup_val', flat=True)
        for rating in EQCascadiaDisplaced_2017_220619_rating:
            EQCascadiaDisplaced_2017_220619_snugget = Snugget.objects.filter(EQCascadiaDisplaced_2017_220619_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if EQCascadiaDisplaced_2017_220619_snugget:
                groupsDict[EQCascadiaDisplaced_2017_220619.getGroup()].extend(EQCascadiaDisplaced_2017_220619_snugget)

        qs_kingco_water = kingco_water.objects.filter(geom__contains=pnt)
        kingco_water_rating = qs_kingco_water.values_list('lookup_val', flat=True)
        for rating in kingco_water_rating:
            kingco_water_snugget = Snugget.objects.filter(kingco_water_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if kingco_water_snugget:
                groupsDict[kingco_water.getGroup()].extend(kingco_water_snugget)

        qs_FloodDamInund_2013_220710 = FloodDamInund_2013_220710.objects.filter(geom__contains=pnt)
        FloodDamInund_2013_220710_rating = qs_FloodDamInund_2013_220710.values_list('lookup_val', flat=True)
        for rating in FloodDamInund_2013_220710_rating:
            FloodDamInund_2013_220710_snugget = Snugget.objects.filter(FloodDamInund_2013_220710_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if FloodDamInund_2013_220710_snugget:
                groupsDict[FloodDamInund_2013_220710.getGroup()].extend(FloodDamInund_2013_220710_snugget)

        qs_kingco_roads = kingco_roads.objects.filter(geom__contains=pnt)
        kingco_roads_rating = qs_kingco_roads.values_list('number', flat=True)
        for rating in kingco_roads_rating:
            kingco_roads_snugget = Snugget.objects.filter(kingco_roads_filter__number__exact=rating).order_by('order').select_subclasses()
            if kingco_roads_snugget:
                groupsDict[kingco_roads.getGroup()].extend(kingco_roads_snugget)

        qs_FloodCMZ_2015_220703 = FloodCMZ_2015_220703.objects.filter(geom__contains=pnt)
        FloodCMZ_2015_220703_rating = qs_FloodCMZ_2015_220703.values_list('lookup_val', flat=True)
        for rating in FloodCMZ_2015_220703_rating:
            FloodCMZ_2015_220703_snugget = Snugget.objects.filter(FloodCMZ_2015_220703_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if FloodCMZ_2015_220703_snugget:
                groupsDict[FloodCMZ_2015_220703.getGroup()].extend(FloodCMZ_2015_220703_snugget)

        qs_kingco_cities = kingco_cities.objects.filter(geom__contains=pnt)
        kingco_cities_rating = qs_kingco_cities.values_list('objectid', flat=True)
        for rating in kingco_cities_rating:
            kingco_cities_snugget = Snugget.objects.filter(kingco_cities_filter__objectid__exact=rating).order_by('order').select_subclasses()
            if kingco_cities_snugget:
                groupsDict[kingco_cities.getGroup()].extend(kingco_cities_snugget)

        qs_Heat_2020_20220803 = Heat_2020_20220803.objects.filter(geom__contains=pnt)
        Heat_2020_20220803_rating = qs_Heat_2020_20220803.values_list('lookup_val', flat=True)
        for rating in Heat_2020_20220803_rating:
            Heat_2020_20220803_snugget = Snugget.objects.filter(Heat_2020_20220803_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Heat_2020_20220803_snugget:
                groupsDict[Heat_2020_20220803.getGroup()].extend(Heat_2020_20220803_snugget)

        qs_poly = poly.objects.filter(geom__contains=pnt)
        poly_rating = qs_poly.values_list('shape_id', flat=True)
        for rating in poly_rating:
            poly_snugget = Snugget.objects.filter(poly_filter__shape_id__exact=rating).order_by('order').select_subclasses()
            if poly_snugget:
                groupsDict[poly.getGroup()].extend(poly_snugget)

        qs_poly_mask = poly_mask.objects.filter(geom__contains=pnt)
        poly_mask_rating = qs_poly_mask.values_list('lookup_val', flat=True)
        for rating in poly_mask_rating:
            poly_mask_snugget = Snugget.objects.filter(poly_mask_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if poly_mask_snugget:
                groupsDict[poly_mask.getGroup()].extend(poly_mask_snugget)

        qs_seattle_kingco = seattle_kingco.objects.filter(geom__contains=pnt)
        seattle_kingco_rating = qs_seattle_kingco.values_list('lookup_val', flat=True)
        for rating in seattle_kingco_rating:
            seattle_kingco_snugget = Snugget.objects.filter(seattle_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if seattle_kingco_snugget:
                groupsDict[seattle_kingco.getGroup()].extend(seattle_kingco_snugget)

        qs_kingco = kingco.objects.filter(geom__contains=pnt)
        kingco_rating = qs_kingco.values_list('lookup_val', flat=True)
        for rating in kingco_rating:
            kingco_snugget = Snugget.objects.filter(kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if kingco_snugget:
                groupsDict[kingco.getGroup()].extend(kingco_snugget)

        qs_Winter_kingco = Winter_kingco.objects.filter(geom__contains=pnt)
        Winter_kingco_rating = qs_Winter_kingco.values_list('lookup_val', flat=True)
        for rating in Winter_kingco_rating:
            Winter_kingco_snugget = Snugget.objects.filter(Winter_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if Winter_kingco_snugget:
                groupsDict[Winter_kingco.getGroup()].extend(Winter_kingco_snugget)

        qs_LS_kingco = LS_kingco.objects.filter(geom__contains=pnt)
        LS_kingco_rating = qs_LS_kingco.values_list('lookup_val', flat=True)
        for rating in LS_kingco_rating:
            LS_kingco_snugget = Snugget.objects.filter(LS_kingco_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            if LS_kingco_snugget:
                groupsDict[LS_kingco.getGroup()].extend(LS_kingco_snugget)

# END OF GENERATED CODE BLOCK
######################################################
        return groupsDict

    def __str__(self):
        return "Snugget base class string."


class TextSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_TEXT]
    content = models.TextField()

    def getRelatedTemplate(self):
        return "snugget_text.html"

    def __str__(self):
        return str(self.content)[:100]


class EmbedSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_VIDEO]
    text = models.TextField(default="")
    video = EmbedVideoField()

    def getRelatedTemplate(self):
        return "snugget_embed.html"

    def __str__(self):
        return "Embed Snugget: " + str(self.video)


class SlideshowSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_SLIDESHOW]
    text = models.TextField(default="")

    def getRelatedTemplate(self):
        return "snugget_slideshow.html"

    def __str__(self):
        return "Slideshow Snugget: " + str(self.text)


class PastEventsPhoto(models.Model):
    snugget = models.ForeignKey(
        SlideshowSnugget, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="photos")
    caption = models.TextField(default="", max_length=200)

    def __str__(self):
        return str(self.image.url) + ' Caption: ' + str(self.caption)


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        self.delete(name)
        return name


class DataOverviewImage(models.Model):
    link_text = models.CharField(default="", max_length=100)
    image = models.ImageField(upload_to="data", storage=OverwriteStorage())

    def __str__(self):
        return self.image.url
