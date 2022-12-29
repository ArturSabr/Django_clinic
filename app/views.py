from django.shortcuts import render,redirect
from .models import *
from  .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import *


def home(request):
    form = EntryForm()
    applicationform = EntryForm()
    return render(request,'index.html',{'applicationform': applicationform })


def doctors(request):
    doctor = Doctors.objects.all()
    return render(request, 'doctor.html', {'doctor': doctor})

def about(request):
    return render(request, 'about_us.html')


def price(request):
    return render(request, 'price.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print('POST')
        if form.is_valid():
            form.save()
            print('Valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            print('hz')
            login(request, user)
            return redirect('/')
        else:
            print(form.errors)
    register_form = UserCreationForm()
    form = EntryForm()
    return render(request,'register.html',{'register_form': register_form })

def more(request, id):
    doctor = Doctors.objects.get(id=id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def add (request):
    form = EntryForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')
