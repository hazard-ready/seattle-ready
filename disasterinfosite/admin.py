from django.contrib.gis import admin
from embed_video.admin import AdminVideoMixin
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminModelImports
from .models import EmbedSnugget, TextSnugget, SnuggetSection, SnuggetSubSection, Location, SiteSettings, SupplyKit, ImportantLink, EQ_Cascadia_kingco, EQ_kingco, EQ_Liquefact_kingco, EQ_Nisqual68_kingco, EQ_SeattleFault72_kingco, EQ_Tsunami_SeaFault72_kingco, EQ_URM_DensityZones_seattle, Fire_kingco, Fire_WUI_kingco_only, Flood_100yr_wUrban_kingco, Flood_500yr_wUrban_kingco, Flood_CMZ_kingco, Flood_DamInundation, Flood_kingco, Flood_nearest_sand_distr, Hubs_Nearest_seattle, LSLD_existing_features, LSLD_ExistingAreas_kingco, LSLD_kingco, LSLD_Prone_kingco, LSLD_steepgradezone_0x0, LSLD_steepgradezone_0x1, LSLD_steepgradezone_1x0, LSLD_steepgradezone_1x1, Summer_kingco, Volcano_kingco, Volcano_Lahar_kingco, Winter_kingco
# END OF GENERATED CODE BLOCK
######################################################
from .models import ShapefileGroup, PastEventsPhoto, DataOverviewImage, UserProfile
from .actions import export_as_csv_action

admin.site.register(SnuggetSection, TranslationAdmin)
admin.site.register(SnuggetSubSection, TranslationAdmin)
admin.site.register(ShapefileGroup, TranslationAdmin)
admin.site.register(PastEventsPhoto, TranslationAdmin)
admin.site.register(DataOverviewImage, TranslationAdmin)


class SnuggetAdmin(admin.ModelAdmin):
######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminLists
    list_display = ('shortname', 'section', 'sub_section', 'EQ_Cascadia_kingco_filter', 'EQ_kingco_filter', 'EQ_Liquefact_kingco_filter', 'EQ_Nisqual68_kingco_filter', 'EQ_SeattleFault72_kingco_filter', 'EQ_Tsunami_SeaFault72_kingco_filter', 'EQ_URM_DensityZones_seattle_filter', 'Fire_kingco_filter', 'Fire_WUI_kingco_only_filter', 'Flood_100yr_wUrban_kingco_filter', 'Flood_500yr_wUrban_kingco_filter', 'Flood_CMZ_kingco_filter', 'Flood_DamInundation_filter', 'Flood_kingco_filter', 'Flood_nearest_sand_distr_filter', 'Hubs_Nearest_seattle_filter', 'LSLD_existing_features_filter', 'LSLD_ExistingAreas_kingco_filter', 'LSLD_kingco_filter', 'LSLD_Prone_kingco_filter', 'Summer_kingco_filter', 'Volcano_kingco_filter', 'Volcano_Lahar_kingco_filter', 'Winter_kingco_filter')
    list_filter = ('section', 'sub_section', 'EQ_Cascadia_kingco_filter', 'EQ_kingco_filter', 'EQ_Liquefact_kingco_filter', 'EQ_Nisqual68_kingco_filter', 'EQ_SeattleFault72_kingco_filter', 'EQ_Tsunami_SeaFault72_kingco_filter', 'EQ_URM_DensityZones_seattle_filter', 'Fire_kingco_filter', 'Fire_WUI_kingco_only_filter', 'Flood_100yr_wUrban_kingco_filter', 'Flood_500yr_wUrban_kingco_filter', 'Flood_CMZ_kingco_filter', 'Flood_DamInundation_filter', 'Flood_kingco_filter', 'Flood_nearest_sand_distr_filter', 'Hubs_Nearest_seattle_filter', 'LSLD_existing_features_filter', 'LSLD_ExistingAreas_kingco_filter', 'LSLD_kingco_filter', 'LSLD_Prone_kingco_filter', 'Summer_kingco_filter', 'Volcano_kingco_filter', 'Volcano_Lahar_kingco_filter', 'Winter_kingco_filter')

    fieldsets = (
        (None, {
            'fields': ('section', 'sub_section')
        }),
        ('Filters', {
            'description': 'Choose a filter value this snugget will show up for.  It is recommended you only select a value for one filter and leave the rest empty.',
            'fields': (('EQ_Cascadia_kingco_filter', 'EQ_kingco_filter', 'EQ_Liquefact_kingco_filter', 'EQ_Nisqual68_kingco_filter', 'EQ_SeattleFault72_kingco_filter', 'EQ_Tsunami_SeaFault72_kingco_filter', 'EQ_URM_DensityZones_seattle_filter', 'Fire_kingco_filter', 'Fire_WUI_kingco_only_filter', 'Flood_100yr_wUrban_kingco_filter', 'Flood_500yr_wUrban_kingco_filter', 'Flood_CMZ_kingco_filter', 'Flood_DamInundation_filter', 'Flood_kingco_filter', 'Flood_nearest_sand_distr_filter', 'Hubs_Nearest_seattle_filter', 'LSLD_existing_features_filter', 'LSLD_ExistingAreas_kingco_filter', 'LSLD_kingco_filter', 'LSLD_Prone_kingco_filter', 'Summer_kingco_filter', 'Volcano_kingco_filter', 'Volcano_Lahar_kingco_filter', 'Winter_kingco_filter'))
        })
    )
# END OF GENERATED CODE BLOCK
######################################################

    def shortname(self, obj):
        return "Undefined"


class TextAdmin(SnuggetAdmin, TranslationAdmin):
    fieldsets = SnuggetAdmin.fieldsets + ((None, {
        'fields': ('content',),
        }),
    )

    def shortname(self, obj):
        return 'Text: "' + str(obj) + '"'


class EmbedAdmin(AdminVideoMixin, SnuggetAdmin):
    fieldsets = SnuggetAdmin.fieldsets + ((None, {
        'fields': ('embed',),
        }),
    )

    def shortname(self, obj):
        return "EmbedSnugget"

admin.site.register(TextSnugget, TextAdmin)
admin.site.register(EmbedSnugget, EmbedAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Users'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    actions = [export_as_csv_action("CSV Export", fields=('username','address1','address2','city','state','zip_code'))]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class GeoNoEditAdmin(admin.GeoModelAdmin):
    modifiable = False

admin.site.register(ImportantLink, TranslationAdmin)
class SiteSettingsAdmin(SingletonModelAdmin, TranslationAdmin):
    pass
admin.site.register(SiteSettings, SiteSettingsAdmin)

class LocationAdmin(SingletonModelAdmin, TranslationAdmin):
    pass
admin.site.register(Location, LocationAdmin)

class SupplyKitAdmin(SingletonModelAdmin, TranslationAdmin):
    pass
admin.site.register(SupplyKit, SupplyKitAdmin)

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminSiteRegistrations
admin.site.register(EQ_Cascadia_kingco, GeoNoEditAdmin)
admin.site.register(EQ_kingco, GeoNoEditAdmin)
admin.site.register(EQ_Liquefact_kingco, GeoNoEditAdmin)
admin.site.register(EQ_Nisqual68_kingco, GeoNoEditAdmin)
admin.site.register(EQ_SeattleFault72_kingco, GeoNoEditAdmin)
admin.site.register(EQ_Tsunami_SeaFault72_kingco, GeoNoEditAdmin)
admin.site.register(EQ_URM_DensityZones_seattle, GeoNoEditAdmin)
admin.site.register(Fire_kingco, GeoNoEditAdmin)
admin.site.register(Fire_WUI_kingco_only, GeoNoEditAdmin)
admin.site.register(Flood_100yr_wUrban_kingco, GeoNoEditAdmin)
admin.site.register(Flood_500yr_wUrban_kingco, GeoNoEditAdmin)
admin.site.register(Flood_CMZ_kingco, GeoNoEditAdmin)
admin.site.register(Flood_DamInundation, GeoNoEditAdmin)
admin.site.register(Flood_kingco, GeoNoEditAdmin)
admin.site.register(Flood_nearest_sand_distr, GeoNoEditAdmin)
admin.site.register(Hubs_Nearest_seattle, GeoNoEditAdmin)
admin.site.register(LSLD_existing_features, GeoNoEditAdmin)
admin.site.register(LSLD_ExistingAreas_kingco, GeoNoEditAdmin)
admin.site.register(LSLD_kingco, GeoNoEditAdmin)
admin.site.register(LSLD_Prone_kingco, GeoNoEditAdmin)
admin.site.register(LSLD_steepgradezone_0x0, GeoNoEditAdmin)
admin.site.register(LSLD_steepgradezone_0x1, GeoNoEditAdmin)
admin.site.register(LSLD_steepgradezone_1x0, GeoNoEditAdmin)
admin.site.register(LSLD_steepgradezone_1x1, GeoNoEditAdmin)
admin.site.register(Summer_kingco, GeoNoEditAdmin)
admin.site.register(Volcano_kingco, GeoNoEditAdmin)
admin.site.register(Volcano_Lahar_kingco, GeoNoEditAdmin)
admin.site.register(Winter_kingco, GeoNoEditAdmin)
# END OF GENERATED CODE BLOCK
######################################################
