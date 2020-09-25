from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from accounts.models import Profile
from friendreq.models import ItemsFound, ItemRequest
from . models import CoordinatedItems, CoordinationForm, close_related_request


def coordinator_create_view(request):
    if request.method == 'GET':
        form = CoordinationForm()
        matchedItems,openRequests, users, profiles = get_data_query_sets()
        return render (request, 'coordinator.html', {'form': form, 'matchedItems':matchedItems, 'openRequests':openRequests, 'users': users})
    else:
        form = CoordinationForm(request.POST or None)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()
            close_related_request(request)
        context = {
            'form' :form
        }
        return redirect('/coordinate')

def filter_coordinator_view(request):

    form = CoordinationForm()
    matchedItems, openRequests, users, profiles = get_data_query_sets()

    item_filter = request.GET.get('item')
    pickup_city_filter = request.GET.get('city_pickup')
    drop_off_city_filter = request.GET.get('city_drop_off')

    if item_filter != "" and item_filter is not None:
        matchedItems = matchedItems.filter(title = item_filter)
    if pickup_city_filter != "" and pickup_city_filter is not None:
        matchedItems = matchedItems.filter(city = pickup_city_filter)
    # if drop_off_city_filter != "" and drop_off_city_filter is not None:
    #     profiles = profiles.filter(address_city = drop_off_city_filter)
    #     for request in openRequests:
    #         if profiles.filter(user = request.User)
    #             print(openRequests.size)
    #             openRequests.exclude(request)
    #             print(openRequests.size)

    return render (request, 'coordinator.html', {'form': form, 'matchedItems':matchedItems, 'openRequests':openRequests, 'users': users})



def get_data_query_sets():
    matchedItems = ItemsFound.objects.filter(match=True)
    openRequests = ItemRequest.objects.filter(status='in_process')
    users = User.objects.all()
    profiles = Profile.objects.all()

    return matchedItems,openRequests,users,profiles

