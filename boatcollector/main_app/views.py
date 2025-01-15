from django.shortcuts import render, redirect
from .models import Boat, Flag
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ServicingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class BoatCreate(LoginRequiredMixin, CreateView):
    model = Boat
    # fields = '__all__
    fields = ['name', 'model', 'description', 'production', 'image']
    success_url = '/boats/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BoatUpdate(LoginRequiredMixin, UpdateView):
    model = Boat
    fields = ['description']
    success_url = '/boats/'

class BoatDelete(LoginRequiredMixin, DeleteView):
    model = Boat
    success_url = '/boats/'

class FlagList(LoginRequiredMixin, ListView):
    model = Flag

class FlagDetail(LoginRequiredMixin, DetailView):
    model = Flag

class FlagCreate(LoginRequiredMixin, CreateView):
    model = Flag
    fields = '__all__'

class FlagUpdate(LoginRequiredMixin, UpdateView):
    model = Flag
    fields = ['name', 'color']

class FlagDelete(LoginRequiredMixin, DeleteView):
    model = Flag
    success_url = '/flags/'


# Define the home view
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def boats_index(request):
    boats = Boat.objects.filter(user=request.user)
    # boats = Boat.objects.all()
    return render(request, 'boats/index.html', { 'boats': boats })

@login_required
def boats_detail(request, boat_id):
    boat = Boat.objects.get(id=boat_id)
    Servicing_form = ServicingForm()
    flags_boat_doesnt_have = Flag.objects.exclude(id__in = boat.flags.all().values_list('id'))
    return render(request, 'boats/detail.html', {'boat': boat, 'Servicing_form': Servicing_form, 
                                                'flags': flags_boat_doesnt_have})

@login_required
def add_servicing(request, boat_id):
    form = ServicingForm(request.POST)
    if form.is_valid():
        new_servicing = form.save(commit=False)
        new_servicing.boat_id = boat_id
        new_servicing.save()
    return redirect('detail', boat_id = boat_id)

@login_required
def assoc_flag(request, boat_id, flag_id):
    Boat.objects.get(id=boat_id).flags.add(flag_id)
    return redirect('detail', boat_id = boat_id)

@login_required
def unassoc_flag(request, boat_id, flag_id):
    Boat.objects.get(id=boat_id).flags.remove(flag_id)
    return redirect('detail', boat_id = boat_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup- please try again later.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render (request, 'registration/signup.html', context)
