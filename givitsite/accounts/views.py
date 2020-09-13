from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .forms import RegistrationForm, PersonInfoForm

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = PersonInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            return redirect('/')
    else:        
        user_form = RegistrationForm()
        profile_form = PersonInfoForm()
    args = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'register.html', args)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

