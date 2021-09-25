from django.shortcuts import redirect, render
from . forms import UserRegister
from django.contrib import messages
from django.contrib.auth import views as auth_view, login

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == "POST":
            form = UserRegister(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                return redirect('home')
        
        else: 
            form = UserRegister()

        return render(request, 'users/register.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        return redirect('home')