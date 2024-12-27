from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def addhotel(request):
    if request.method == 'POST':
        hotelName = request.POST['hotelName']
        location = request.POST['location']
        hotelType = request.POST['hotelType']
        rating = request.POST['rating']
        contact = request.POST['contact']
        address = request.POST['address']
        hotel_image = request.FILES['hotel_image']
        # save data to the hotel table
        new_hotel = Hotel(
            hotelName=hotelName,
            location=location,
            hotelType=hotelType,
            rating=rating,
            contact=contact,
            address=address,
            hotel_image=hotel_image
        )
        new_hotel.save()
        
        return render(request, 'hotelapp/success.html', {'hotel': new_hotel, 'success_message': 'Hotel Added Successfuly!'})
    
    else:
        return render(request, 'hotelapp/AddHotel.html')

def showHotel(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotelapp/hotellist.html', {'hotels': hotels})

def updateHotels(request):
    if request.method == 'POST':
        # Use the same variable names as in addhotel
        hotelName = request.POST['hotelName']
        location = request.POST['location']
        hotelType = request.POST['hotelType']
        rating = request.POST['rating']
        contact = request.POST['contact']
        address = request.POST['address']
        hotelId = request.POST['hotelId']  # Assuming this is passed in the form
        hotel_image = request.FILES.get('hotel_image')

        # Retrieve the hotel instance
        try:
            hotel = Hotel.objects.get(hotelId=hotelId)
            # Update the fields
            hotel.hotelName = hotelName
            hotel.location = location
            hotel.hotelType = hotelType
            hotel.rating = rating
            hotel.contact = contact
            hotel.address = address
            
            # Only update the image if a new one is provided
            if hotel_image:
                hotel.hotel_image = hotel_image
            
            # Save the updated instance
            hotel.save()

            # Render the success template with the updated hotel information
            # return render(request, 'hotelapp/update_form.html', {'hotel': hotel, 'success_message': 'Update successful!'})
            return render(request, 'hotelapp/success.html', {'hotel':hotel, 'success_message': 'Hotel Updated Successfuly!'})
        except Hotel.DoesNotExist:
            return HttpResponse("<h1>Hotel not found</h1>")
    else:
        # Render the update form if the request method is not POST
        return render(request, 'hotelapp/update_form.html')
    

def editHotels(request, id):
        data=Hotel.objects.get(hotelId=id)
        return render(request, 'hotelapp/update_form.html', {'hotel': data})