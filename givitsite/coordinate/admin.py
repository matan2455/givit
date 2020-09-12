import sys
from django.contrib import admin
from . models import CoordinatedItems

sys.path.append('../')
admin.site.register(CoordinatedItems)


