from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from . models import Records
from . form import RecordForm
# Create your views here.

def home(request):
    # Check to see if logging in
    records = Records.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, 'There was an error loggin in, please try again....')
            return redirect('home')
    return render(request, 'website/home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have benn logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.create_user(first_name = name, last_name = lastname, email= email, username= username, password=password)
            messages.success(request, 'Your user have been created!!')
            return redirect('home')
        except Exception as e:
            messages.success(request, 'There was an error creating your user, try again')
            return render(request, 'website/regist.html')


    return render(request, 'website/regist.html')

def records(request, pk):
    if request.user.is_authenticated:
        records = Records.objects.filter(id = pk).all()
        return render(request, 'website/custom_record.html', {'records': records})
    else:
        messages.success(request, 'You must be logged in!!')
        return render(request, 'website/home.html')

def edit_record(request, pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Records, id=pk)
        
        if request.method == 'POST':
            # Actualizar cada campo manualmente
            record.first_name = request.POST.get('name', record.first_name)
            record.last_name = request.POST.get('lastname', record.last_name)
            record.email = request.POST.get('email', record.email)
            record.phone = request.POST.get('phone', record.phone)
            record.adress = request.POST.get('adress', record.adress)
            record.city = request.POST.get('city', record.city)
            record.state = request.POST.get('state', record.state)
            record.zipcode = request.POST.get('zipcode', record.zipcode)
            
            try:
                record.save()
                messages.success(request, "Record updated successfully!")
                return redirect('records', pk=pk)
            except Exception as e:
                messages.error(request, f"Error updating record: {e}")
        
        # Si es GET, mostrar el formulario con los datos actuales
        return redirect('records', pk=pk)
    else:
        messages.success(request, 'You must be logged in!!')
        return redirect('home')

def delete_record(request, pk):
    if request.method == 'POST':
        record = Records.objects.get(id = pk)
        record.delete()
        messages.success(request, 'Record deleted')
        return redirect('home')

def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The record has been created')
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else: 
        form = RecordForm()
    return render(request, 'website/create_record.html', {'form': form})

def search_record(request):
    if request.method == 'POST':
        name = request.POST['name']
        records = Records.objects.filter(first_name = name).all()
        print(type(records))
        return render(request, 'website/home.html', {'records': records})
