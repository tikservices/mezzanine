from modeltranslation.translator import translator, TranslationOptions
from mezzanine.conf.models import Setting
from mezzanine.conf import settings


class TranslatedSetting(TranslationOptions):
    fields = ('value',)


if settings.USE_MODELTRANSLATION:
    translator.register(Setting, TranslatedSetting)
