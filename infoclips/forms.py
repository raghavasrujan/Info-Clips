from django import forms


class UrlForm(forms.Form):

    url = forms.CharField(
        required=False, 
        label="Enter Url",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    


class SearchForm(forms.Form):

    search = forms.CharField(
    required=False ,
    label="Search Term",
    widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    