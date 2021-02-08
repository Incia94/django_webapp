from django.shortcuts import render
from django.http import HttpResponse
from booking.models import Booking


# Create your views here.
def Greetings(request):
    return render(request, 'website/Greetings.html',
                  {"bookings": Booking.objects.count()})


def about(request):
    return HttpResponse("Book your table today to have an amazing culinary experience!")
