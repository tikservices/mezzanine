from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import (TranslatedDisplayable,
                                        TranslatedRichText)
from mezzanine.pages.models import Page, RichTextPage, Link
from mezzanine.conf import settings


class TranslatedPage(TranslatedDisplayable):
    fields = ('titles',)


class TranslatedRichTextPage(TranslatedRichText):
    fields = ()


class TranslatedLink(TranslationOptions):
    fields = ()


if settings.USE_MODELTRANSLATION:
    translator.register(Page, TranslatedPage)
    translator.register(RichTextPage, TranslatedRichTextPage)
    translator.register(Link, TranslatedLink)
