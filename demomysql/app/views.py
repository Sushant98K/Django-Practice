from django.shortcuts import render
from .models import *
# Create your views here.
def adddata(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        
        new = Demodata(name=name, age=age, email=email)
        new.save()
        
        return render(request, 'app/success.html', {'data': new})
    else:
        return render(request, 'app/index.html')

def showdata(request):
    data = Demodata.objects.all()
    return render(request, 'app/showdata.html', {'data': data})