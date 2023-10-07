from django.shortcuts import render,redirect
from .form import *
from django.contrib import messages

from .models import *

# Create your views here.

def index(request):
    p = Profile.objects.all()
    context = {
        'p':p
    }
    return render(request, 'new_app/index.html',context) 

def contact(request):
    form = Contact_f(request.POST)
    if request.method == 'POST':
        form = Contact_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('/')
        else:
            form =Contact_f()
            return render(request,'new_app/contact.html')
    context={
        'form': form,
    } 
    return render(request, 'new_app/contact.html',context)


def projects(request):
    return render(request, 'new_app/projects.html')
def resume(request):
    return render(request, 'new_app/resume.html')

