from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RedirectsConfig(AppConfig):

    name = "redirects"
    verbose_name = _("Redirects")
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        pass
