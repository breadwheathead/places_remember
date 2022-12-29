from django import forms

from remembersapp.models import Remember


class RememberAddForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = ('title', 'description', 'latitude', 'longitude')

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите название места'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'rows': 5, 'placeholder': 'Введите описание'}))
    latitude = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'lat', 'readonly': True}))
    longitude = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'lon', 'readonly': True}))
