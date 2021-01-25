from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import TranslatedRichText
from mezzanine.galleries.models import GalleryImage, Gallery
from mezzanine.conf import settings


class TranslatedGallery(TranslatedRichText):
    fields = ()


class TranslatedGalleryImage(TranslationOptions):
    fields = ('description',)


if settings.USE_MODELTRANSLATION:
    translator.register(Gallery, TranslatedGallery)
    translator.register(GalleryImage, TranslatedGalleryImage)
