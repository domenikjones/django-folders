# -*- coding: utf-8 -*-
from django.contrib import admin
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext

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

    actions = ['add_to_folder']

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

    def add_to_folder(self, request, queryset):
        class FolderSelectForm(forms.Form):
            _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
            folder = FolderModelChoiceField(queryset=Folder.objects.all(),
                                            label="Ordner")

        form = None

        if 'apply' in request.POST:
            form = FolderSelectForm(request.POST)

            if form.is_valid():
                folder = form.cleaned_data['folder']

                for obj in queryset:
                    obj.folder = folder
                    obj.save()

                self.message_user(
                    request,
                    ("{model_label} wurden erfolgreich in den Ordner '{folder}' "
                     "verschoben.").format(
                        model_label=queryset.model._meta.verbose_name_plural,
                        folder=folder.name,
                    )
                )
                return HttpResponseRedirect(request.get_full_path())

        if not form:
            form = FolderSelectForm(
                initial={
                    '_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
                }
            )

        return render_to_response(
            'folders/add_to_folder.html',
            {
                'objects': queryset,
                'form': form,
            },
            context_instance=RequestContext(request),
        )
    add_to_folder.short_description = "In Ordner verschieben"
