from django import forms
from .models import UploadFiles
from django.forms import ClearableFileInput

class FilesUpload(forms.Form):
    upload_to = forms.CharField(max_length = 100)
    upload_folder = forms.CharField(max_length = 100)
    upload_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
class FilesUpload1(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['upload_files']
        widgets = {
            'upload_files': ClearableFileInput(attrs={'multiple': True}),
        }

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()