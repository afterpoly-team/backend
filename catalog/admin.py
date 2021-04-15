from django import forms
from django.contrib import admin
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent
from modeltranslation.admin import TranslationAdmin


# admin.site.register(Address)
admin.site.register(OnlineEvent, TranslationAdmin)
admin.site.register(Place, TranslationAdmin)
admin.site.register(RealLifeEvent, TranslationAdmin)
admin.site.register(Tag, TranslationAdmin)
admin.site.register(Address, TranslationAdmin)


#     list_display = ('title', 'creation_date',
#                     'description', 'event_date', 'link', )


# @admin.register(Address)
# class AddressAdmin(TranslationAdmin):
#     list_display = ('country', 'city', 'district', 'region',
#                     'house_number', 'street', 'corps')


# @admin.register(OnlineEvent)
# class OnlineEventAdmin(admin.ModelAdmin):
#     list_display = ('__all__')


# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('__all__')


# @admin.register(RealLifeEvent)
# class RealLifeEventAdmin():
#     list_display = ('__all__')


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name',)


admin.site.site_title = "AfterPoly administration"
admin.site.site_header = "AfterPoly administration"
