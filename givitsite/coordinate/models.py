from django.db import models
from django import forms
from friendreq.models import REGION_CHOICES, ITEM_CHOICES , ItemRequest 


STATUS_CHOICES = [
    ('coordinated', 'coordinated'),
    ('waiting', 'waiting')
]

class CoordinatedItems(models.Model):
    friend_id = models.CharField(max_length = 40, default = 305355356)
    request_id = models.IntegerField(default = 1234)
    date = models.DateField(auto_now=False, auto_now_add=False)
    pickup_time = models.TimeField(auto_now=False, auto_now_add=False)
    drop_off_time = models.TimeField(auto_now=False, auto_now_add=False)
    item = models.CharField(max_length = 40,choices = ITEM_CHOICES)
    pickup_location = models.CharField(max_length = 40,choices = REGION_CHOICES)
    drop_off_location = models.CharField(max_length = 40,choices = REGION_CHOICES)
    status = models.CharField(max_length = 40,default = 'waiting', choices = STATUS_CHOICES)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CoordinationForm(forms.ModelForm):
    class Meta:
        model = CoordinatedItems
        widgets = {
            'date' : DateInput(),
            'pickup_time': TimeInput(),
            'drop_off_time' : TimeInput()
        }
        fields = [
            'friend_id',
            'request_id',
            'item',
            'pickup_location',
            'drop_off_location',   
            'date',
            'pickup_time',
            'drop_off_time',
            'status'
            ]

def create_new_coordinations(request):
    form = CoordinationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            fs =form.save(commit=False)
            fs.friend_id = request.user
            fs.save()
        context = {
            'form' :form
        }

def close_related_request(request):
    ItemRequest.objects.filter(id = request.POST['request_id']).update(status='close')

