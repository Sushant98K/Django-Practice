from django.urls import path
from .views import *

urlpatterns = [
    path('addhotel/', addhotel, name='addhotel'),
]