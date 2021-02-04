from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Greetings(request):
    return HttpResponse("Welcome to Cafe Incia!")


def about(request):
    return HttpResponse("Book your table today to have an amazing culinary experience!")
