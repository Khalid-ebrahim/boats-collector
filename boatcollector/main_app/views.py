from django.shortcuts import render, redirect
from .models import Boat, Flag
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ServicingForm
from django.views.generic import ListView, DetailView

class BoatCreate(CreateView):
    model = Boat
    # fields = '__all__
    fields = ['name', 'model', 'description', 'production', 'image']
    success_url = '/boats/'

class BoatUpdate(UpdateView):
    model = Boat
    fields = ['description']
    success_url = '/boats/'

class BoatDelete(DeleteView):
    model = Boat
    success_url = '/boats/'

class FlagList(ListView):
    model = Flag

class FlagDetail(DetailView):
    model = Flag

class FlagCreate(CreateView):
    model = Flag
    fields = '__all__'

class FlagUpdate(UpdateView):
    model = Flag
    fields = ['name', 'color']

class FlagDelete(DeleteView):
    model = Flag
    success_url = '/flags/'


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
    flags_boat_doesnt_have = Flag.objects.exclude(id__in = boat.flags.all().values_list('id'))
    return render(request, 'boats/detail.html', {'boat': boat, 'Servicing_form': Servicing_form, 
                                                'flags': flags_boat_doesnt_have})


def add_servicing(request, boat_id):
    form = ServicingForm(request.POST)
    if form.is_valid():
        new_servicing = form.save(commit=False)
        new_servicing.boat_id = boat_id
        new_servicing.save()
    return redirect('detail', boat_id = boat_id)

def assoc_flag(request, boat_id, flag_id):
    Boat.objects.get(id=boat_id).flags.add(flag_id)
    return redirect('detail', boat_id = boat_id)

def unassoc_flag(request, boat_id, flag_id):
    Boat.objects.get(id=boat_id).flags.remove(flag_id)
    return redirect('detail', boat_id = boat_id)