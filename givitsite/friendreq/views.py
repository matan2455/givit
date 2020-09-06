from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemRequest
from .models import ItemsFound
from .forms import itemRequestForm

# Create your views here.

def itemRequest_create_view(request):
    form = itemRequestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            fs =form.save(commit=False)
            fs.friend_id = request.user
            fs.save()
        context = {
            'form' :form
        }
        return render(request,"demandDB.html",context)
    else:
        context = {
        'form' :form
        }    
        return render(request, 'itemRequestform.html',context)


def requestItem(request):
    # on match
    if request.method == 'POST':
        id = request.POST["id"]
        matchItem = ItemsFound.objects.filter(pk=id).update(match=True)

    founditems = ItemsFound.objects.all()
    allrequests = ItemRequest.objects.all()
    return render (request, 'feed.html', {'founds':founditems, 'allRequests':allrequests})

