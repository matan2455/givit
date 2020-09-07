import sys
import os
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404
from django.contrib.auth.models import User
from friendreq.models import ItemsFound
from friendreq.models import ItemRequest
from django.conf import settings
from . models import CoordinatedItems


# Create your views here.
def coordinator_create_view(request):
    
    if request.method == 'GET':
        itemsToCoordinate = []
        matchedItems = ItemsFound.objects.filter(match=True)
        openRequests = ItemRequest.objects.filter(status='open')
        users = User.objects.all()
        

        # mock data for testing:

        # itemsToCoordinate.append({
        #     "item":'chair',
        #     "pickup_location":'Tel Aviv',
        #     "drop_off_location":'Jerusalem',
        #     "url": 'https://www.etzmaleh.co.il/Media/Uploads/tn_%D7%9B%D7%99%D7%A1%D7%90_%D7%95%D7%A0%D7%A6%D7%99%D7%94_%D7%AA%D7%9B%D7%9C%D7%AA.jpg_op1_690x920(15).jpg',
        #     "friend_id":"1234",
        #     "picture": '',
        #     "request_id": '1',
        #     "user_id": '2'
        # })

        # itemsToCoordinate.append({
        #     "item":'chair',
        #     "pickup_location":'Jerusalem',
        #     "drop_off_location":'Tel Aviv',
        #     "url": 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRxJI6_VVfFWUPcvozhhY7qNVWaujOLj1zI8A&usqp=CAU',
        #     "friend_id":"1235",
        #     "picture": '',
        #     "request_id": '2',
        #     "user_id": '3'
        # })

        return render (request, 'coordinator.html', {'matchedItems':matchedItems, 'openRequests':openRequests, 'users': users})

    elif request.method == 'POST':
        save_to_coordinations(request);
        update_friendreq_db(request);
        return redirect('/coordinate')
    
   

def save_to_coordinations(request):

    print("Times:")
    print(request.POST['pickup_time']);
    print(request.POST['drop_off_time']);

    request_id = request.POST['request_id']

    if request.method == 'POST':
        CoordinatedItems.objects.create(
            friend_id = request.POST['friend_id'],
            request_id = request.POST['request_id'], 
            pickup_location = request.POST['pickup_location'],
            drop_off_location = request.POST['drop_off_location'],
            item = request.POST['item'],
            date = request.POST['date'],
            pickup_time = request.POST['pickup_time'],
            drop_off_time = request.POST['drop_off_time'],
            status = 'coordinated'
            ) 
    

def update_friendreq_db(request):
    ItemRequest.objects.filter(id = request.POST['request_id']).update(status='closed')


def test(request):
    print(sys.path)
    return render (request, 'home.html')


def create_file(request):
    fh = open('brief.txt', 'w+')
    date_of_transfer = request.POST['date']
    print(date_of_transfer)
    fh.write('brief for transfer date - '+ date_of_transfer + '\n\n')
    itemsForBrief = CoordinatedItems.objects.all(); #filter(date = date_of_transfer)
    count = 1;

    for item in itemsForBrief: #.objects.filter(date = date_of_transfer):
        item_title = "item number " + str(count) + '\n'
        fh.write(item_title)
        fh.write(
                    'item: ' + item.item + '\n' +
                    'pick up from: ' + item.pickup_location + '\n' +
                    'drop_off_location: ' + item.drop_off_location + '\n' +
                    'pickup_time ' + item.pickup_time.strftime("%H:%M:%S") + '\n' +
                    'drop_off_time ' + item.drop_off_time.strftime("%H:%M:%S") + '\n\n'
                    )
        count = count + 1
        
    fh.close();
    return redirect('/coordinate')


def download_file(request):
    print("test")
    file_path = 'givitsite/brief'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.txt")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    print("not found the file")
    raise Http404


