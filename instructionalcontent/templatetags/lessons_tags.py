from django import template
from django.conf import settings

register = template.Library()

tabs = (
    ('Overview', 'Directions', 'Objectives', 'Background & Vocabulary', 'Credits, Sponsors, Partners'),
    ('Global Metadata', 'Content Related Metadata', 'Time and Date Metadata', 'Publishing'),
)

@register.filter(name='tab_num')
def tab_num(fieldset):
    for count, fieldsets in enumerate(tabs):
        if fieldset.name in fieldsets:
            return count
    return 0

def get_model(field, setting):
    for name, model in settings.LESSON_SETTINGS[setting]:
        if field == name:
            return model
    return None

@register.filter(name='get_activity_model')
def get_activity_model(field):
    return get_model(field, 'ACTIVITY_FIELDS')

@register.filter(name='get_lesson_model')
def get_lesson_model(field):
    return get_model(field, 'LESSON_FIELDS')
