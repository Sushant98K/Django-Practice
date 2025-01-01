from django.urls import path
from .views import *

urlpatterns = [
    path("booking/<int:id>", addBooking, name="booking"),
    path("bookinglist/", bookingList, name="bookinglist"),
    path("bookinglist/delete/<int:id>/", deleteBooking, name="deletebooking"),
]