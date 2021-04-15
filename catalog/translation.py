from modeltranslation.translator import translator, register, TranslationOptions
from .models import Event, Tag, OnlineEvent, Address, Place, RealLifeEvent


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description',
              'organizers', 'additional_information')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('country', 'city', 'district', 'region', 'street', )


translator.register(Place)
translator.register(RealLifeEvent)
translator.register(OnlineEvent)
