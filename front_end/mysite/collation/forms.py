from django import forms

class DataQueryForm(forms.Form):
    civil = forms.BooleanField(label='civil', required=False)
    criminal = forms.BooleanField(label='criminal', required=False)