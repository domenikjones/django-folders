from django import forms

from .fields import FolderModelChoiceField
from .models import Folder


class FolderAdminForm(forms.ModelForm):
    parent = FolderModelChoiceField(queryset=Folder.objects.all(), required=False,
                                    label="Elternordner")

    class Meta:
        model = Folder
        fields = ('parent', 'name')
