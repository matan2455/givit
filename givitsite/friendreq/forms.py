from django import forms

from . models import ItemRequest

class itemRequestForm(forms.ModelForm):
    class Meta:
        model = ItemRequest
        fields = [
            'item',
            'region',
            'special_req'
        ]
