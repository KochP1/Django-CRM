from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    # Check to see if logging in

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
    return render(request, 'website/home.html', {})

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