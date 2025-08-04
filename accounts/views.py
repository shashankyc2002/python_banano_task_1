from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard_view(request):
    if request.user.user_type == 'doctor':
        return render(request, 'doctor_dashboard.html', {'user': request.user})
    else:
        return render(request, 'patient_dashboard.html', {'user': request.user})
