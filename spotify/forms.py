from django import forms
from .models import Playlist

class CreatePlaylistForm(forms.ModelForm):
    # name = forms.CharField()
    # img = forms.ImageField()
    #
    # def __str__(self):
    #     return self.name
    class Meta:
        model = Playlist
        fields = ['name', 'image', 'music']

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'My playlist'})
        }