from django.shortcuts import render, redirect
from .models import Boat
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ServicingForm
from django.views.generic import ListView

class BoatCreate(CreateView):
    model = Boat
    # fields = '__all__
    fields = ['name', 'model', 'description', 'production', 'image']

class BoatUpdate(UpdateView):
    model = Boat
    fields = ['description']
    success_url = '/boats/'

class BoatDelete(DeleteView):
    model = Boat
    success_url = '/boats/'

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello boat</h1>')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
    boats = Boat.objects.all()
    return render(request, 'boats/index.html', { 'boats': boats })

def boats_detail(request, boat_id):
    boat = Boat.objects.get(id=boat_id)
    Servicing_form = ServicingForm()
    return render(request, 'boats/detail.html', {'boat': boat, 'Servicing_form': Servicing_form})


def add_servicing(request, boat_id):
    form = ServicingForm(request.POST)
    if form.is_valid():
        new_servicing = form.save(commit=False)
        new_servicing.boat_id = boat_id
        new_servicing.save()
    return redirect('detail', boat_id = boat_id)