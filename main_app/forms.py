from django.forms import ModelForm
from .models import Mixing

class MixingForm(ModelForm):
    class Meta:
        model = Mixing
        fields = ['date', 'color']