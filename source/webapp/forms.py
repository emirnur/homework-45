from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class TrackerForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Title')
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label='Status')
    deadline = forms.DateField(required=False, label='Deadline', widget=widgets.TextInput(
        attrs={'placeholder':'введите в формате YYYY-MM-DD'}))