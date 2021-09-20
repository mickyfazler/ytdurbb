from django import forms

class ContractFormBB(forms.Form):
    namey=forms.CharField(max_length=100)
    starting_number=forms.IntegerField()            # not give NumberInput 
    ending_number=forms.IntegerField() 