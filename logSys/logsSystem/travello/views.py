from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = "Tehran"
    dest1.desc = "Best city eva"
    dest1.price = 1234
    dest1.img = "destination_1.jpg"
    dest1.offer = True

    dest2 = Destination()
    dest2.name = "SC"
    dest2.desc = "Basdfasdfasdfasdf"
    dest2.price = 2
    dest2.img = "destination_2.jpg"
    dest2.offer = False


    dests = [dest1,dest2]

    return render(request, 'index.html', {'dests': dests} )