from django.shortcuts import render

# Create your views here.

from .models import Flight


def index(request):
    flights = Flight.objects.all()
    # context = flights
    return render(request, "flights/index.html", {"flights": flights})


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {
                  "flight": flight,
                  "passengers": passengers
                  })

def book(request):
    