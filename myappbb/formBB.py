from django import forms
# don't forget to import them baby...genius... don't give up
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _ 

class ContractFormBB(forms.Form):
    # namey=forms.CharField(max_length=100)
    # starting_number=forms.IntegerField()            # not give NumberInput 
    # ending_number=forms.IntegerField() 
    namey=forms.CharField(max_length=100,label=_("Youtube Playlist Link"),widget=widgets.TextInput(attrs={'autofocus': True,"class" : "form-control"}))            # learned from `Geekyshows Django Code\All codes\122\prog122\myapp\formy.py`
    starting_number=forms.IntegerField(widget=widgets.TextInput(attrs={'autofocus': True,"class" : "form-control",'type':"number"}))            # not give NumberInput ....'type':"number" learned from chatgpt 
    ending_number=forms.IntegerField(widget=widgets.TextInput(attrs={'autofocus': True,"class" : "form-control",'type':"number"})) 