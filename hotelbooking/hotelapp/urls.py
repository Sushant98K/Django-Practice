from django.urls import path
from .views import *

urlpatterns = [
    path('addhotel/', addhotel, name='addhotel'),
    path('show/', showHotel, name='showhotel'),
    path('updatehotel/', updateHotels, name='updatehotel'),
    path('show/edit/<int:id>', editHotels, name='edit'),
    path('show/delete/<int:id>', deleteHotels, name='delete'),
]