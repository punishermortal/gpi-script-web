from django import forms

class FileUploadForm(forms.Form):
    file1 = forms.FileField(label="Upload File 1", required=True)
    file2 = forms.FileField(label="Upload File 2", required=True)
    file3 = forms.FileField(label="Upload File 3", required=True)
    file4 = forms.FileField(label="Upload File 4", required=True)
