from friendreq.models import ItemsFound, ItemRequest, STATUS_CHOICES as REQUEST_STATUS_CHOICES
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import CoordinatedItems
from django.conf import settings
from . import constants
import sys
import os


def coordinator_create_view(request):
    if request.method == 'GET':
        itemsToCoordinate = []
        matchedItems = ItemsFound.objects.filter(match=True)
        openRequests = ItemRequest.objects.filter(status=constants.request_status_open)
        users = User.objects.all()

        return render (request, 'coordinator.html', {'matchedItems':matchedItems, 'openRequests':openRequests, 'users': users})
    else:
        create_new_coordinations(request);
        close_related_request(request);
        return redirect('/coordinate')
    

def create_new_coordinations(request):
    request_id = request.POST[constants.request_id]
    if request.method == 'POST':
        CoordinatedItems.objects.create(
            friend_id = request.POST[constants.friend_id],
            request_id = request.POST[constants.request_id], 
            pickup_location = request.POST[constants.pickup_location],
            drop_off_location = request.POST[constants.drop_off_location],
            item = request.POST[constants.item],
            date = request.POST[constants.date],
            pickup_time = request.POST[constants.pickup_time],
            drop_off_time = request.POST[constants.drop_off_time],
            status = constants.item_status_coordinated
            ) 


def close_related_request(request):
    ItemRequest.objects.filter(id = request.POST[constants.request_id]).update(status=constants.request_status_closed)


def create_delivery_brief(request):  
    fh = open('brief.txt', 'w+')
    date_of_transfer = request.POST[constants.date]

    fh.write('brief for transfer date - ' + date_of_transfer + '\n\n')
    itemsForBrief = CoordinatedItems.objects.all(); 
    itemNumber = 1;

    for item in itemsForBrief: 
        item_title = "item number " + str(itemNumber) + '\n'
        fh.write(item_title)
        fh.write(
                constants.item_title + item.item + '\n' +
                constants.pickup_location_title + item.pickup_location + '\n' +
                constants.drop_off_location_title + item.drop_off_location + '\n' +
                constants.pickup_time_title + item.pickup_time.strftime(constants.time_format) + '\n' +
                constants.drop_off_time_title + item.drop_off_time.strftime(constants.time_format) + '\n\n'
                )
        itemNumber = itemNumber + 1   
    fh.close();
    return redirect('/coordinate')
    
