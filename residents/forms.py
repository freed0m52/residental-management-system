from django import forms
from .models import Request, Resident
from premises.models import Premise


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["resident", "premise", "request_type", "description", "status"]


class PremiseForm(forms.ModelForm):
    class Meta:
        model = Premise
        fields = ["number", "premise_type", "area"]


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ["full_name", "apartment_number", "phone", "status"]
