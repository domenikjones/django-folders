from django import forms
from django.utils.translation import ugettext_lazy as _

from .fields import FolderModelChoiceField
from .models import Folder


class FolderAdminForm(forms.ModelForm):
    parent = FolderModelChoiceField(queryset=Folder.objects.none(), required=False,
                                    label=_("Elternordner"))

    def __init__(self, *args, **kwargs):
        super(FolderAdminForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Folder.objects.all()

    class Meta:
        model = Folder
        fields = ('parent', 'name')
