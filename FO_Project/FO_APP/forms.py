from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.shortcuts import render
from .models import Payment

class CoffeePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit', 'Buy', css_class='btn btn-primary mx-auto d-block')
        )
