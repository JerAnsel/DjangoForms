from django.forms import ModelForm
import django.forms as forms

class FlavorForm(forms.Form):
    username = forms.CharField(label='Name: ', widget=forms.TextInput(attrs={'maxlength': 50, 'class':'form_input'}))
    flavor = forms.CharField(label='Favorite Ice Cream Flavor: ', widget=forms.TextInput(attrs={'maxlength': 100, 'class':'form_input'}))

