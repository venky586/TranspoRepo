from django import forms

from .models import CabDetails

class PostForm(forms.ModelForm):

    class Meta:
        model = CabDetails
        fields = ('title', 'text',)