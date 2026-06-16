from django.shortcuts import render, redirect
from .models import Apartments, Category, Booking
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    apartments = Apartments.objects.all()
    return render(request, 'index.html', {'name': 'Booking App', 'apartments': apartments})


def booking(request, apartment_id):

    apartments = Apartments.objects.get(id=apartment_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        booking = Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            apartment=apartments,
            check_in=check_in,
            check_out=check_out,
            user=request.user if request.user.is_authenticated else None    
        )


        return redirect('booking_confirmation', booking_id=booking.id)

    context = {"apart": apartments}
    return render(request, 'booking.html', context)


def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    apartment = booking.apartment
    return render(request, 'booking_confirmed.html', {'booking': booking, 'apart': apartment})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'user_bookings.html', {'bookings': bookings})