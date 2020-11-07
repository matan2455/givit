from django.shortcuts import redirect, render
from friendreq.models import (ITEM_CHOICES, REGION_CHOICES, ItemRequest,
                              ItemsFound)

from .models import CoordinatedItems, CoordinationForm, close_related_request


def coordinator_create_view(request):
    if request.method == 'GET':
        form = CoordinationForm()
        matchedItems, openRequests = get_data_query_sets(request)
        item_choices_list, region_choices_list = get_filters_as_lists()
        render_dict = {
            'form': form,
            'matchedItems': matchedItems,
            'openRequests': openRequests,
            'region_choices': region_choices_list,
            'item_choices': item_choices_list
        }

        return render(request, 'coordinator.html', render_dict)
    else:
        form = CoordinationForm(request.POST or None)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.save()
            close_related_request(request)

        return redirect('/coordinate')


def render_coordinated_items(request):
    date = request.GET.get('shipment_date')
    allCoordinations = CoordinatedItems.objects.filter(transfer_date=date)
    coordinatedObjectsDataList = []
    for item in allCoordinations:
        itemFound = ItemsFound.objects.filter(
            request_id=item.request_id).first()
        itemRequest = ItemRequest.objects.get(pk=item.request_id.id)
        render_dict = {
            'transfer_date': item.transfer_date,
            'item': item.item,
            'student': itemRequest.User,
            'pickup_location': item.pickup_location,
            'pickup_time': item.pickup_time,
            'drop_off_location': item.drop_off_location,
            'drop_off_time': item.drop_off_time,
            'url': itemFound.url,
            'picture': itemFound.picture
        }

        coordinatedObjectsDataList.append(render_dict)
    return render(request, 'schedualedItems.html',
                  {'coordinatedObjectsDataList': coordinatedObjectsDataList})


def get_filters_as_lists():
    item_choices_list = []
    region_choices_list = []

    for region in REGION_CHOICES:
        region_choices_list.append(region[1])
    for item in ITEM_CHOICES:
        item_choices_list.append(item[1])
    return item_choices_list, region_choices_list


def get_data_query_sets(request):
    matchedItems = ItemsFound.objects.filter(match=True)
    openRequests = ItemRequest.objects.filter(status='in_process')
    item_filter = request.GET.get('item')
    pickup_city_filter = request.GET.get('city_pickup')
    if item_filter is not None and item_filter != "":
        matchedItems = matchedItems.filter(title=item_filter)
    if (pickup_city_filter is not None) and (pickup_city_filter != ""):
        matchedItems = matchedItems.filter(city=pickup_city_filter)
    return matchedItems, openRequests
