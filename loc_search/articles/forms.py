from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import ExpertArticle


class ExpertArticleAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = ExpertArticle
        fields = "__all__"
