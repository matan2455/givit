from django.db import models
from django import forms
from friendreq.models import REGION_CHOICES, ITEM_CHOICES , ItemRequest 



class CoordinatedItems(models.Model): 
    #request ID inherite from ItemRequest table  
    request_id = models.OneToOneField(ItemRequest, on_delete=models.CASCADE ) 
    item = models.CharField(max_length = 40,choices = ITEM_CHOICES)
    transfer_date = models.DateField(auto_now=False, auto_now_add=False)
    student_phone_number = models.CharField(max_length = 10)
    pickup_time = models.TimeField(auto_now=False, auto_now_add=False)
    pickup_location = models.CharField(max_length = 40,choices = REGION_CHOICES)
    drop_off_time = models.TimeField(auto_now=False, auto_now_add=False)
    drop_off_location = models.CharField(max_length = 40,choices = REGION_CHOICES)



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CoordinationForm(forms.ModelForm):
    class Meta:
        model = CoordinatedItems
        widgets = {
            'transfer_date' : DateInput(),
            'pickup_time': TimeInput(),
            'drop_off_time' : TimeInput()
        }
        fields = [
            'item',
            'transfer_date',
            'request_id',
            'pickup_location',
            'drop_off_location',   
            'student_phone_number',
            'pickup_time',
            'drop_off_time'
            ]


def close_related_request(request):
    ItemRequest.objects.filter(id = request.POST['request_id']).update(status='closed')


