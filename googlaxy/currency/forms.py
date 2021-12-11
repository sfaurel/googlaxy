from django import forms


class GooglaxyForm(forms.Form):
    question = forms.CharField(max_length=500)


class AddItemForm(forms.Form):
    name = forms.CharField(max_length=500)
    price = forms.IntegerField()


class AddNumeralForm(forms.Form):
    name = forms.CharField(max_length=500)
    roman = forms.CharField(max_length=1)
