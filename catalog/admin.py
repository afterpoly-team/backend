from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'creation_date',
                    'description', 'event_date', 'link', )

# Register your models here.
