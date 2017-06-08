from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.gdal import GDALRaster
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import Extent
from embed_video.fields import EmbedVideoField
from model_utils.managers import InheritanceManager
from solo.models import SingletonModel
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import pre_save
from django.dispatch import receiver

SNUG_TEXT = 0
SNUG_AUDIO = 1
SNUG_VID = 2

SNUGGET_TYPES = (
                 ('SNUG_TEXT', 'TextSnugget'),
                 )
class UserProfile(models.Model):
    """ A model representing a user's information that isn't their username, password, or email address """
    user = models.OneToOneField(User)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return "{0}: {1}, {2} {3}, {4} {5}".format(self.user, self.address1, self.address2, self.city, self.state, self.zip_code)


class SiteSettings(SingletonModel):
    """A singleton model to represent site-wide settings."""
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
    intro_text= models.TextField(
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
    area_name = models.CharField(
        max_length=100,
        default="the affected area",
        help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'."
    )

    community_leaders = models.TextField(
        default="Information about community leaders goes here.",
        help_text="Information about community leaders, how to contact them, and form groups."
    )

    def __unicode__(self):
        return u"Location Information"

    @staticmethod
    def get_data_bounds():
        bounds = {
    ######################################################
    # GENERATED CODE GOES HERE
    # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
    # locationsList
            'LSLD_steepgradezone': LSLD_steepgradezone.objects.data_bounds(),
            'Summer_kingco': Summer_kingco.objects.data_bounds(),
            'Volcano_kingco': Volcano_kingco.objects.data_bounds(),
            'Volcano_Lahar_kingco': Volcano_Lahar_kingco.objects.data_bounds(),
            'Winter_kingco': Winter_kingco.objects.data_bounds()
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
            west.append(box[0])
            south.append(box[1])
            east.append(box[2])
            north.append(box[3])

        # The largest box that contains all the bounding boxes, how Leaflet wants it.
        return [[min(south), min(west)], [max(north), max(east)]]


    class Meta:
        verbose_name = "Location Information"

class SupplyKit(SingletonModel):
    """ A singleton model representing the supply kit information """
    days = models.PositiveIntegerField(
        default=3,
        help_text="The number of days' worth of supplies prepared residents should have on hand."
    )
    text = models.TextField(
        help_text="More information about building your supply kit. Any web address in here gets turned into a link automatically."
    )

class ImportantLink(models.Model):
    """ A model representing a link with a title """
    title = models.CharField(
        max_length=50,
        help_text="A title for your important link, like 'Evacuation Information'"
    )
    link = models.TextField(
        help_text="Your link and any information about it. Any web address in here gets turned into a link automatically."
    )
    def __str__(self):
        return self.title +': ' + self.link

class ShapeManager(models.GeoManager):
    def has_point(self, pnt):
        return self.filter(geom__contains=pnt)

    def data_bounds(self):
        return self.aggregate(Extent('geom'))['geom__extent']

class RasterManager(models.GeoManager):
    def has_point(self, pnt):
        return self.filter(rast__contains=pnt)

    def data_bounds(self):
        return self.aggregate(Extent('rast'))['rast__extent']

class ShapefileGroup(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, default="")
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order, from left to right, in which you would like this group to appear, when applicable."
    )
    likely_scenario_title = models.CharField(max_length=80, blank=True)
    likely_scenario_text = models.TextField(blank=True)

    def __str__(self):
        return self.name

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsClasses
class LSLD_steepgradezone(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='quake')[0]

    rast = models.RasterField()
    objects = RasterManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup)
    def __str__(self):
        return str(self.bands[0])

class Summer_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='summer')[0]

    lookup_val = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup)
    def __str__(self):
        return str(self.lookup_val)

class Volcano_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='volcano')[0]

    lookup_val = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup)
    def __str__(self):
        return str(self.lookup_val)

class Volcano_Lahar_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='volcano')[0]

    lookup_val = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup)
    def __str__(self):
        return str(self.lookup_val)

class Winter_kingco(models.Model):
    def getGroup():
        return ShapefileGroup.objects.get_or_create(name='winter')[0]

    lookup_val = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    group = models.ForeignKey(ShapefileGroup, default=getGroup)
    def __str__(self):
        return str(self.lookup_val)

# END OF GENERATED CODE BLOCK
######################################################

class RecoveryLevels(models.Model):
    name = models.CharField(max_length=50)
    shortLabel = models.CharField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Infrastructure(models.Model):
    name = models.CharField(max_length=255)
    eventOccursRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    firstDayRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threeDaysRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    sevenDaysRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    fourWeeksRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threeMonthsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    sixMonthsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    twelveMonthsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threeYearsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threePlusYearsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name + " in " + str(self.zone)


class InfrastructureGroup(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Infrastructure)

    def __str__(self):
        return self.name


class InfrastructureCategory(models.Model):
    name = models.CharField(max_length=50)
    groups = models.ManyToManyField(InfrastructureGroup)

    def __str__(self):
        return self.name + " in " + str(self.zone)


class SnuggetType(models.Model):
    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=255, choices=SNUGGET_TYPES)

    def __str__(self):
        return self.name


class SnuggetSection(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, help_text="The name to show for this section", default="")
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order in which you'd like this to appear in the tab. 0 is at the top."
    )

    def __str__(self):
        return self.name

class SnuggetSubSection(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, help_text="The name to show for this section", default="")
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order in which you'd like this to appear in the section. 0 is at the top. These can be in different sections or mutually exclusive, hence the non-unique values."
    )

    def __str__(self):
        return self.name

@receiver(pre_save, sender=SnuggetSection)
@receiver(pre_save, sender=SnuggetSection)
@receiver(pre_save, sender=ShapefileGroup)
def default_display_name(sender, instance, *args, **kwargs):
    if not instance.display_name:
        instance.display_name = instance.name


class Snugget(models.Model):
    objects = InheritanceManager()

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsFilters
    LSLD_steepgradezone_filter = models.ForeignKey(LSLD_steepgradezone, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Summer_kingco_filter = models.ForeignKey(Summer_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Volcano_kingco_filter = models.ForeignKey(Volcano_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Volcano_Lahar_kingco_filter = models.ForeignKey(Volcano_Lahar_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Winter_kingco_filter = models.ForeignKey(Winter_kingco, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
# END OF GENERATED CODE BLOCK
######################################################

    section = models.ForeignKey(SnuggetSection, related_name='+', on_delete=models.PROTECT)
    sub_section = models.ForeignKey(SnuggetSubSection, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    group = models.ForeignKey(ShapefileGroup, on_delete=models.PROTECT, null=True)

    def getRelatedTemplate(self):
        return "snugget.html"

    @staticmethod
    def findSnuggetsForPoint(lat=0, lng=0, merge_deform = True):
        pnt = Point(lng, lat)
        groups = ShapefileGroup.objects.all()
        groupsDict = {}

        for group in groups:
            groupsDict[group.name] = []

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsGeoFilters
        qs_LSLD_steepgradezone = LSLD_steepgradezone.objects.filter(geom__contains=pnt)
        LSLD_steepgradezone_rating = qs_LSLD_steepgradezone.values_list('bands[0]', flat=True)
        for rating in LSLD_steepgradezone_rating:
            individualSnugget = Snugget.objects.filter(LSLD_steepgradezone_filter__exact=rating).select_subclasses()
            if individualSnugget:
                groupsDict[individualSnugget[0].group.name].extend(individualSnugget)

        qs_Summer_kingco = Summer_kingco.objects.filter(geom__contains=pnt)
        Summer_kingco_rating = qs_Summer_kingco.values_list('lookup_val', flat=True)
        for rating in Summer_kingco_rating:
            individualSnugget = Snugget.objects.filter(Summer_kingco_filter__lookup_val__exact=rating).select_subclasses()
            if individualSnugget:
                groupsDict[individualSnugget[0].group.name].extend(individualSnugget)

        qs_Volcano_kingco = Volcano_kingco.objects.filter(geom__contains=pnt)
        Volcano_kingco_rating = qs_Volcano_kingco.values_list('lookup_val', flat=True)
        for rating in Volcano_kingco_rating:
            individualSnugget = Snugget.objects.filter(Volcano_kingco_filter__lookup_val__exact=rating).select_subclasses()
            if individualSnugget:
                groupsDict[individualSnugget[0].group.name].extend(individualSnugget)

        qs_Volcano_Lahar_kingco = Volcano_Lahar_kingco.objects.filter(geom__contains=pnt)
        Volcano_Lahar_kingco_rating = qs_Volcano_Lahar_kingco.values_list('lookup_val', flat=True)
        for rating in Volcano_Lahar_kingco_rating:
            individualSnugget = Snugget.objects.filter(Volcano_Lahar_kingco_filter__lookup_val__exact=rating).select_subclasses()
            if individualSnugget:
                groupsDict[individualSnugget[0].group.name].extend(individualSnugget)

        qs_Winter_kingco = Winter_kingco.objects.filter(geom__contains=pnt)
        Winter_kingco_rating = qs_Winter_kingco.values_list('lookup_val', flat=True)
        for rating in Winter_kingco_rating:
            individualSnugget = Snugget.objects.filter(Winter_kingco_filter__lookup_val__exact=rating).select_subclasses()
            if individualSnugget:
                groupsDict[individualSnugget[0].group.name].extend(individualSnugget)


        return {'groups': groupsDict,
                'LSLD_steepgradezone_rating': LSLD_steepgradezone_rating,
                'Summer_kingco_rating': Summer_kingco_rating,
                'Volcano_kingco_rating': Volcano_kingco_rating,
                'Volcano_Lahar_kingco_rating': Volcano_Lahar_kingco_rating,
                'Winter_kingco_rating': Winter_kingco_rating
                }
# END OF GENERATED CODE BLOCK
######################################################



    def __str__(self):
        return "Snugget base class string."


class TextSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_TEXT]
    content = models.TextField()
    image = models.TextField(default="")
    percentage = models.FloatField(null=True)

    def getRelatedTemplate(self):
        return "snugget_text.html"

    def __str__(self):
        return str(self.content)[:100]


class EmbedSnugget(Snugget):
    embed = EmbedVideoField()

    def getRelatedTemplate(self):
        return "snugget_embed.html"

    def __str__(self):
        return "Embed Snugget: " + str(self.embed)

class PastEventsPhoto(models.Model):
    group = models.ForeignKey(ShapefileGroup, on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to="photos")
    caption = models.TextField(default="", max_length=500)

    def __str__(self):
        return self.image.url

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        self.delete(name)
        return name

class DataOverviewImage(models.Model):
    link_text = models.CharField(default="", max_length=100)
    image = models.ImageField(upload_to="data", storage=OverwriteStorage())

    def __str__(self):
        return self.image.url
