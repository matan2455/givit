import sys
from django.contrib import admin
from . models import CoordinatedItems

# Register your models here.
sys.path.append('../')
admin.site.register(CoordinatedItems)

