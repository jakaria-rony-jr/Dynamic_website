from django.shortcuts import render, redirect
from .forms import UserRegistrationForm



def index(request):
    return render(request, 'main_app/index.html')

def Registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'main_app/registration.html', {'form': form})


from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Change 'home' to your desired login success URL
    return render(request, 'main_app/login.html')