from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import TranslatedRichText
from mezzanine.forms.models import Form, Field
from mezzanine.conf import settings


class TranslatedForm(TranslatedRichText):
    fields = ('button_text', 'response', 'email_subject', 'email_message',)


class TranslatedField(TranslationOptions):
    fields = ('label', 'choices', 'default', 'placeholder_text', 'help_text',)


if settings.USE_MODELTRANSLATION:
    translator.register(Form, TranslatedForm)
    translator.register(Field, TranslatedField)
