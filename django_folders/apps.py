from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoFoldersConfig(AppConfig):
    name = 'django_folders'
    verbose_name = _("Folders")
