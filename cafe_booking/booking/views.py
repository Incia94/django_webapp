from django.shortcuts import render, get_object_or_404
from .models import Booking
from django.db import migrations


# Create your views here.

def booking_detail(request, id):
    book = get_object_or_404(Booking, pk=id)
    # book = Booking.objects.get(pk=id)
    return render(request, "booking/detail.html", {"booking": book})
