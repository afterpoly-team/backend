from django import forms
from django.contrib import admin
from .models import Event
from modeltranslation.admin import TranslationAdmin


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ('title', 'creation_date',
                    'description', 'event_date', 'link', )

# Register your models here.
