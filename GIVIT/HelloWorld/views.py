from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return render(request, "web/index.html") 

    # return HttpResponse("Hello, world. from GIVIT")