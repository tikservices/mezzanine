from modeltranslation.translator import translator
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from mezzanine.blog.models import BlogCategory, BlogPost
from mezzanine.conf import settings


class TranslatedBlogPost(TranslatedDisplayable, TranslatedRichText):
    fields = ()


class TranslatedBlogCategory(TranslatedSlugged):
    fields = ()


if settings.USE_MODELTRANSLATION:
    translator.register(BlogCategory, TranslatedBlogCategory)
    translator.register(BlogPost, TranslatedBlogPost)
