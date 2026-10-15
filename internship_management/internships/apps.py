from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InternshipsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "internship_management.internships"
    verbose_name = _("Internships")
