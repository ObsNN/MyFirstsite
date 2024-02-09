from django import forms

from .models import Music

class PostForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ('title', 'text',)