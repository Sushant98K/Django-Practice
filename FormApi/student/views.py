from django.shortcuts import render
from .forms import *

# Create your views here.
def register(request):
    # fm = Registrations(auto_id='id_%s') here you can change ID of the fiels like id='something' where id is writen
    
    # fm = Registrations(auto_id=True) here you can change id to same as label 
    
    # fm = Registrations(label_suffix='a') it will replace : from a
    
    # fm = Registrations(initial={'first_name': 'John', 'last_name': 'Doe'}) here you can give your default value 
    
    # fm = Registrations(field_order=['first_name', 'last_name','ciy','email']) you can change the order here

    fm = Registrations()
    
    return render(request, 'student/index.html', {'form': fm})