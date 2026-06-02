from django.shortcuts import render
from .models import Apartments, Category, Booking

# Create your views here.
def home(request):
    apartments = Apartments.objects.all()
    return render(request, 'index.html', {'name': 'Booking App', 'apartments': apartments})


def booking(request, apartment_id):

    apartments = Apartments.objects.get(id=apartment_id)
    context = {"apart": apartments}

    return render(request, 'booking.html', context)