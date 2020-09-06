from django.db import models
from friendreq.models import REGION_CHOICES 
from friendreq.models import ITEM_CHOICES


STATUS_CHOICES = [
    ('coordinated', 'coordinated'),
    ('waiting', 'waiting')
]


class CoordinatedItems(models.Model):
    #friennd ID inherite from user table
    friend_id = models.IntegerField(default = 305355356)
    request_id = models.IntegerField(default = 1234)
    date = models.DateField(auto_now=True, auto_now_add=False)
    pickup_time = models.TimeField(auto_now=True, auto_now_add=False)
    drop_off_time = models.TimeField(auto_now=True, auto_now_add=False)
    item = models.CharField(max_length = 40,choices = ITEM_CHOICES)
    pickup_location = models.CharField(max_length = 40,choices = REGION_CHOICES)
    drop_off_location = models.CharField(max_length = 40,choices = REGION_CHOICES)
    status = models.CharField(max_length = 40,default = 'waiting', choices = STATUS_CHOICES)


