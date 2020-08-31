from django.db import models

# Create your models here.

class ItemRequest(models.Model):
    friend_id = models.IntegerField()
    item = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)
    special_req= models.TextField()
    isOpen = models.BooleanField(default = True)
    