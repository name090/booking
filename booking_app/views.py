from django.shortcuts import render
from .models import Apartments, Category, Booking

# Create your views here.
def home(request):
    apartments = Apartments.objects.all()
    return render(request, 'index.html', {'name': 'Booking App', 'apartments': apartments})