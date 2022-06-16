from .models import Comment
from django import forms
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        labels = {
            'body': _('Komentarz'),
            'name':_('Nazwa Użytkownika'),
        }