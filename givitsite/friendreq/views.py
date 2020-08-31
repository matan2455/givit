from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemRequest

# Create your views here.

def requestItem(request):
    if request.method == 'GET':
        return render(request, 'request.html')

    else:
        city_val = request.POST["city"]
        item_val = request.POST["item"]
        special_val = request.POST["specialreq"]
        newReq = ItemRequest(item=item_val,city = city_val,special_req = special_val,friend_id = 305355356)
        newReq.save();
        print('new item added')
        return render(request, 'demandDB.html')
        
