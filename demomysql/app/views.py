from django.shortcuts import render

# Create your views here.
def adddata(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        return render(request, 'app/success.html', {'name': name, 'age': age, 'email': email})
    else:
        return render(request, 'app/index.html')