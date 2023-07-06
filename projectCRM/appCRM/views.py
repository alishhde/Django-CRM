from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    context = {

    }

    # Check to see if user is logging in (on the other words, if user is posting data)
    if request.method == 'POST':
        username = request.POST['username']  # The 'username' is what we have defined in our form in home.html
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.success(request, "Invalid username or password")
            return redirect('home')

    else:
        return render(request, 'home.html', context)


def logout_user(request):
    context = {

    }
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')