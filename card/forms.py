from .models import Card
from django import forms

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"


class CardGenerateForm(forms.Form):
    series = forms.IntegerField()
    quantity = forms.IntegerField()