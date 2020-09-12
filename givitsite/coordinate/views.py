from friendreq.models import ItemsFound, ItemRequest, STATUS_CHOICES as REQUEST_STATUS_CHOICES
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from . models import CoordinatedItems,CoordinationForm, create_new_coordinations, close_related_request
import sys
import os


def coordinator_create_view(request):
    if request.method == 'GET':
        form = CoordinationForm()
        matchedItems = ItemsFound.objects.filter(match=True)
        openRequests = ItemRequest.objects.filter(status='open')
        users = User.objects.all()
        return render (request, 'coordinator.html', {'form': form, 'matchedItems':matchedItems, 'openRequests':openRequests, 'users': users})
    else:
        form = CoordinationForm(request.POST or None)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()
            close_related_request(request);
        context = {
            'form' :form
        }
        return redirect('/coordinate')
