from django.contrib import admin

from .fields import FolderModelChoiceField
from .forms import FolderAdminForm
from .models import Folder


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    form = FolderAdminForm
    change_form_template = 'folders/change_form.html'


class FolderAdminMixin(object):
    change_form_template = 'folders/change_form.html'
    change_list_template = 'folders/change_list.html'

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'folder':
            return FolderModelChoiceField(queryset=Folder.objects.all(),
                                          required=False,
                                          label="Ordner")
        return super(FolderAdminMixin, self).formfield_for_dbfield(
            db_field, **kwargs)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        folder_id = request.GET.get('folder__id')

        try:
            extra_context['current_folder'] = Folder.objects.get(pk=folder_id)
        except Folder.DoesNotExist:
            extra_context['folder_children'] = Folder.objects.filter(parent__isnull=True)
        else:
            extra_context['folder_children'] = (
                extra_context['current_folder'].children.all())

        return super(FolderAdminMixin, self).changelist_view(
            request, extra_context=extra_context)
