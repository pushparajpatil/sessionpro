from django import forms
class Nameform(forms.Form):
    name=forms.CharField()
class Ageform(forms.Form):
    age=forms.IntegerField()
class Gfform(forms.Form):
    gf=forms.CharField()


