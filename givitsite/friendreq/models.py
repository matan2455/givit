from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

REGION_CHOICES = [
    ('Tel Aviv','Tel Aviv'),
    ('Jerusalem','Jerusalem'),
    ('Beer Sheva','Beer Sheva'),
    ('Haifa','Haifa'),
    ('Modiin','Modiin'),
    ('Hasharon','Hasharon'),
]

ITEM_CHOICES = [
    ('20009','closet'),
    ('20016','bed'),
    ('20008', 'chair'),
    ('10006','fridge'),
    ('10029','Washing machine'),
    ('20017','sofa'),
    

]
STATUS_CHOICES = [
    ('open','open'),
    ('closed','closed'),
    ('in_process', 'in process')
]


class ItemRequest(models.Model):
    User= settings.AUTH_USER_MODEL
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length = 40,choices = ITEM_CHOICES, default='20009')
    region = models.CharField(max_length = 40,choices = REGION_CHOICES, default='Tel Aviv')
    special_req= models.TextField()
    status = models.CharField(max_length = 40,default = 'open', choices = STATUS_CHOICES)
    

class ItemsFound(models.Model):
    request_id = models.ForeignKey(ItemRequest, on_delete=models.CASCADE)
    url = models.URLField()
    picture = models.URLField()
    city = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    match = models.BooleanField(default=False)
