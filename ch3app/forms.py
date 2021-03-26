from django import forms
class UploadFileForm(forms.Form):
    path = forms.CharField(max_length=30)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
