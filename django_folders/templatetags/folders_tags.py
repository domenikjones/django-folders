from django import template
from django.core.urlresolvers import reverse

from ..models import Folder


register = template.Library()


def get_current_folder(context):
    try:
        return context['current_folder']
    except KeyError:
        pass
    try:
        return context['original'].folder
    except (KeyError, AttributeError):
        pass
    try:
        return context['original'].parent
    except (KeyError, AttributeError):
        pass
    folder_id = context['request'].GET.get('folder')
    folder_id = folder_id or context['request'].GET.get('parent')
    try:
        return Folder.objects.get(pk=folder_id)
    except Folder.DoesNotExist:
        return None


@register.inclusion_tag('folders/admin_breadcrumbs.html', takes_context=True)
def show_breadcrumbs(context, model):
    current_folder = get_current_folder(context)

    return {
        'current_folder': current_folder,
        'link_to_current_folder': 'original' in context,
        'model_label': model._meta.verbose_name_plural,
        'app_url': reverse('admin:app_list', kwargs={'app_label': model._meta.app_label}),
        'app_label': model._meta.app_config.verbose_name,
        'changelist_url': reverse('admin:{app}_{model}_changelist'.format(
            app=model._meta.app_label, model=model._meta.model_name)),
    }
