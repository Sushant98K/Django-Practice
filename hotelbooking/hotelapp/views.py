from django.shortcuts import render
from .models import *

# Create your views here.
def addhotel(request):
    if request.method == 'POST':
        hotelName = request.POST['hotelName']
        location = request.POST['location']
        hotelType = request.POST['hotelType']
        rating = request.POST['rating']
        contact = request.POST['contact']
        hotel_image = request.FILES['hotel_image']
        # save data to the hotel table
        new_hotel = Hotel(
            hotelName=hotelName,
            location=location,
            hotelType=hotelType,
            rating=rating,
            contact=contact,
            hotel_image=hotel_image
        )
        # new_hotel.save()
        
        return render(request, 'hotelapp/success.html', {'hotel': new_hotel})
    
    else:
        return render(request, 'hotelapp/AddHotel.html')