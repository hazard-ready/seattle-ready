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
from .models import EmbedSnugget, TextSnugget, SnuggetSection, SnuggetSubSection, Location, SiteSettings, SupplyKit, ImportantLink, LSLD_steepgradezone, Summer_kingco, Volcano_kingco, Volcano_Lahar_kingco, Winter_kingco
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
    list_display = ('shortname', 'section', 'sub_section', 'LSLD_steepgradezone_filter', 'Summer_kingco_filter', 'Volcano_kingco_filter', 'Volcano_Lahar_kingco_filter', 'Winter_kingco_filter')
    list_filter = ('section', 'sub_section', 'LSLD_steepgradezone_filter', 'Summer_kingco_filter', 'Volcano_kingco_filter', 'Volcano_Lahar_kingco_filter', 'Winter_kingco_filter')

    fieldsets = (
        (None, {
            'fields': ('section', 'sub_section')
        }),
        ('Filters', {
            'description': 'Choose a filter value this snugget will show up for.  It is recommended you only select a value for one filter and leave the rest empty.',
            'fields': (('LSLD_steepgradezone_filter', 'Summer_kingco_filter', 'Volcano_kingco_filter', 'Volcano_Lahar_kingco_filter', 'Winter_kingco_filter'))
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
admin.site.register(LSLD_steepgradezone, GeoNoEditAdmin)
admin.site.register(Summer_kingco, GeoNoEditAdmin)
admin.site.register(Volcano_kingco, GeoNoEditAdmin)
admin.site.register(Volcano_Lahar_kingco, GeoNoEditAdmin)
admin.site.register(Winter_kingco, GeoNoEditAdmin)
# END OF GENERATED CODE BLOCK
######################################################
