from django import forms
from django.db import ProgrammingError


class FolderModelChoiceField(forms.ModelChoiceField):
    def _get_choices(self):
        try:
            folders = list(self.queryset.all())
        except ProgrammingError:
            # folder table hasn't been created yet -> need to run migrations
            folders = []

        folders.sort()
        self._choices = [(None, '--------')] + [
            folder.get_form_choice_tuple() for folder in folders
        ]
        return self._choices

    choices = property(_get_choices, forms.ChoiceField._set_choices)
