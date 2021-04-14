from modeltranslation.translator import register, TranslationOptions
from .models import Event, Tag


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name', )
