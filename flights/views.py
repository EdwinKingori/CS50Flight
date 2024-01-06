from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Flight, Passenger


def index(request):
    flights = Flight.objects.all()
    # context = flights
    return render(request, "flights/index.html", {"flights": flights})


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
                  "flight": flight,
                  "passengers": passengers,
                  "non_passengers": non_passengers
                  })


def book(request, flight_id):
    # for a post request, add a new flight
    if request.method == "POST":

        # Access the flight
        flight = Flight.objects.get(pk=flight_id)

        # finding the passenger id from submited form data
        passenger_id = int(request.POST["passenger"])

        # finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Adding passenger to the flight
        passenger.flights.add(flight)

        # redirecting use to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
