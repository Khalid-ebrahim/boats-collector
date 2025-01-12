from django.shortcuts import render
from .models import Boat




# Define the home view
def home(request):
  return render('<h1>Hello boat</h1>')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
    boats = Boat.objects.all()
    return render(request, 'boats/index.html', { 'boats': boats })

def boats_detail(request, boat_id):
    boat = Boat.objects.get(id=boat_id)
    return render(request, 'boats/detail.html', {'boat': boat})