from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm
from . models import Record


def home(request):
    records = Record.objects.all()

    context = {
        'records': records,
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


def register_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered and Signed in.")
            return redirect('home')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up records
        custom_record = Record.objects.get(id=pk)
        context = {
            'customer_record': custom_record,
        }

        return render(request, 'record.html', context)
    else:
        messages.success(request, "You are not Logged in...")
        return redirect('home')

