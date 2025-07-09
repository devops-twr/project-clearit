from django import forms
from .models import Callback
from .models import SyllabusRequest

class CallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ['name', 'email', 'number', 'message']




class SyllabusRequestForm(forms.ModelForm):
    class Meta:
        model = SyllabusRequest
        fields = ['name', 'email', 'mobile', 'city', 'course']