from django.forms import ModelForm, TextInput, CheckboxInput
from .models import Site, Supposition, Response
from django import forms

class PilotForm(ModelForm):
    class Meta:
        model = Site
        fields = ['url']
        widgets = {'url' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Url Address'})}

    class SuppositionForm:
        model = Supposition
        fields = ['note','importance','details']
        #,'steps_to_manifest','screenshot']
        widgets = {
            'note':TextInput(attrs={'class' : 'input', 'placeholder' : 'text'}),
            'importance':forms.NumberInput(attrs={'minlength': 1, 'maxlength': 2, 'required':       True, 'type': 'number',}),
            'details':TextInput(attrs={'class' : 'input', 'placeholder' : 'text'}),
            #'steps_to_manifest':,
            #'screenshot':,
        }

    class ResponseForm:
        model = Response
        fields = ['needs_clarification','in_progress','check_again','fixed','note']
        widgets = {
            'needs_clarification' : CheckboxInput(attrs={'class': 'checkbox'}),
            'in_progess' : CheckboxInput(attrs={'class': 'checkbox'}),
            'check_again' : CheckboxInput(attrs={'class': 'checkbox'}),
            'fixed' : CheckboxInput(attrs={'class': 'checkbox'}),
            'note' : TextInput(attrs={'class' : 'input', 'placeholder' : 'text'}),
        }
