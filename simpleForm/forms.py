from django import forms

class NameForm(forms.Form):
    #first_name = forms.CharField(label='First Parameter', max_length=100)
    first_value = forms.IntegerField(label="First Parameter", min_value= 0, max_value=18)
    second_value = forms.IntegerField(label="Second Parameter", min_value= 0, max_value=3)
    third_value = forms.IntegerField(label="Third Parameter", min_value= 30, max_value=56)