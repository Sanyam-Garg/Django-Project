from django import forms 
from django.core import validators # For validating a form
from . import models

# class user_form(forms.Form):

    # email_field = forms.EmailField()
    # confirm_email = forms.EmailField()

    # def clean(self): # Function name should be clean only (default).
    #     all_cleaned_data = super().clean()

    #     email_field = all_cleaned_data['email_field']
    #     confirm_email = all_cleaned_data['confirm_email']

    #     if email_field != confirm_email:
    #         raise forms.ValidationError('Emails dont match')

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    # If we want to further modify the input fields, use the same name as they are in the table
    release_date = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}))
    class Meta:
        model = models.Album
        fields = '__all__'        
    