from django import forms

class GooglaxyForm(forms.Form):
    question = forms.CharField( max_length=500)