from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent
from modeltranslation.admin import TranslationAdmin


# TODO: add list of dates as function parcing JSON

# * CONSTANTS
DISPLAY_FILEDS_EVENT_INHERITORS = ('title', 'short_description',
                                   'organizers', 'get_main_image')
READONLY_FIELDS_EVENT_INHERITORS = ('get_main_image', 'get_background_image')
MAIN_IMG_DESC = 'Main image representation'
BG_IMP_DESC = 'Background image representation'

# * REGISTATION

admin.site.register(Tag, TranslationAdmin)


# * ADDRESS
@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ('country', 'city', 'district', 'region',
                    'house_number', 'street', 'corps')


# * ONLINE EVENT
@admin.register(OnlineEvent)
class OnlineEventAdmin(TranslationAdmin):
    list_display = DISPLAY_FILEDS_EVENT_INHERITORS
    readonly_fields = READONLY_FIELDS_EVENT_INHERITORS

    def get_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="70" height="50"')

    def get_background_image(self, obj):
        return mark_safe(f'<img src={obj.background_image.url} width="100" height="70"')

    get_main_image.short_description = MAIN_IMG_DESC
    get_background_image.short_description = BG_IMP_DESC


# * PLACE
@admin.register(Place)
class PlaceAdmin(TranslationAdmin):
    list_display = DISPLAY_FILEDS_EVENT_INHERITORS
    readonly_fields = READONLY_FIELDS_EVENT_INHERITORS

    def get_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="70" height="50"')

    def get_background_image(self, obj):
        return mark_safe(f'<img src={obj.background_image.url} width="100" height="70"')

    get_main_image.short_description = MAIN_IMG_DESC
    get_background_image.short_description = BG_IMP_DESC


# * REAL LIFE EVENT
@admin.register(RealLifeEvent)
class RealLifeEventAdmin(TranslationAdmin):
    list_display = DISPLAY_FILEDS_EVENT_INHERITORS
    readonly_fields = READONLY_FIELDS_EVENT_INHERITORS

    def get_main_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="70" height="50"')

    def get_background_image(self, obj):
        return mark_safe(f'<img src={obj.background_image.url} width="100" height="70"')

    get_main_image.short_description = MAIN_IMG_DESC
    get_background_image.short_description = BG_IMP_DESC


# * ADMIN PANEL NAME
admin.site.site_title = "AfterPoly administration"
admin.site.site_header = "AfterPoly administration"
