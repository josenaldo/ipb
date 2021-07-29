from django.conf import settings as django_settings



def social_settings(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'SOCIAL': django_settings.SOCIAL
    }



# def settings(request):
#     settings_in_templates = {}
#     for attr in ["SOCIAL"]:
#         if (hasattr(django_settings, attr)):
#             settings_in_templates[attr] = getattr(django_settings, attr)
#     return {
#         'settings': settings_in_templates,
#     }