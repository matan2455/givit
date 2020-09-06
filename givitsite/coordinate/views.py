import sys
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from givitsite.friendreq.models import ItemRequest
# from ..registration.models import Users
# from sys.path.get import ItemRequest
from friendreq.models import ItemsFound
from friendreq.models import ItemRequest
from . models import CoordinatedItems


# Create your views here.
def coordinator_create_view(request):
    
    if request.method == 'GET':
        itemsToCoordinate = []
        matchedItems = ItemsFound.objects.all() #filter(matched='true')
      
        #test add a new item
        itemsToCoordinate.append({
            "item":'chair',
            "pickup_location":'Tel Aviv',
            "drop_off_location":'Jerusalem',
            "url": 'https://www.etzmaleh.co.il/Media/Uploads/tn_%D7%9B%D7%99%D7%A1%D7%90_%D7%95%D7%A0%D7%A6%D7%99%D7%94_%D7%AA%D7%9B%D7%9C%D7%AA.jpg_op1_690x920(15).jpg',
            "friend_id":"1234",
            "picture": '',
            "phone_number": '0537257325',
            "request_id": '1',
            "user_id": '2'
        })

        itemsToCoordinate.append({
            "item":'chair',
            "pickup_location":'Jerusalem',
            "drop_off_location":'Tel Aviv',
            "url": 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRxJI6_VVfFWUPcvozhhY7qNVWaujOLj1zI8A&usqp=CAU',
            "friend_id":"1235",
            "picture": '',
            "phone_number": '0537257325',
            "request_id": '2',
            "user_id": '3'
        })

        for item in matchedItems:
            print("test")
            for request in ItemRequest.objects.filter(status='open', request_id=item.id):
                print("test")
                itemsToCoordinate.append({
                    "item":item.title,
                    "pickup_location":item.city,
                    "drop_off_location":'Jerusalem',#insert user city
                    "url": item.url,
                    "friend_id":"1234", #user.id
                    "picture": item.picture,
                    "phone_number": item.phone_number,
                    "request_id": request.request.id,
                    "user_id":request.client_id
                })

        return render (request, 'coordinator.html', {'itemsToCoordinate':itemsToCoordinate})

    elif request.method == 'POST':
        save_to_coordinations(request);
        update_friendreq_db(request);
        return redirect('/coordinate')
    
   

def save_to_coordinations(request):

    request_id = request.POST['request_id']
    # phone_number = ItemRequest.objects.filter(id=request.POST['request_id']).get("phone_number")
    print("look!!!")
    # print(request.POST['friend_id'])
    print(request)
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
            # phone_number = phone_number,
            # special_notes = request.POST['special_notes']
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
    items_for_brief = CoordinatedItems.objects.all(); #filter(date = date_of_transfer)
    count = 1;

    for item in items_for_brief: #.objects.filter(date = date_of_transfer):
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

def sync_found_items(request):

    itemsToCoordinate = ItemsFound.objects.all #ItemsFound.objects.filter(match=true)
    allRequests = ItemRequest.objects.all()
    for item in itemsToCoordinate:
        for request in allRequests.objects.filter(request_id=item.id, status='open'):
            # temp until tal kind merge
            friend = [{
                
            }] 
            # friend = Users.objects.filter(friend_id = request.friend_id)
            CoordinatedItems.objects.create(friend.first_name, item = item.title, region_pick_up = item.city,
                region_drop_of = friend.address, status = 'waiting')

