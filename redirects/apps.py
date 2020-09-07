# -*- coding: utf-8 -*-

import django
from django.apps import AppConfig
if django.VERSION < (2, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class RedirectsConfig(AppConfig):

    name = 'redirects'
    verbose_name = _('Redirects')

    def ready(self):
        pass
