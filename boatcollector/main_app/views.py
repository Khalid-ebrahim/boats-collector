from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello boat</h1>')

def about(request):
    return render(request, 'about.html')

def boats_index(request):
  return render(request, 'boats/index.html', { 'boats': boats })

class Boat:  
  def __init__(self, name, model, description, production):
    self.name = name
    self.model = model
    self.description = description
    self.production = production

boats = [
  Boat('Serendipity', 2018, 'full speed', 'yacht'),
  Boat('harry', 2022, 'family boat', 'Fishing boat'),
  Boat('Raff', 1999, 'fishing boat', 'Kayak')
]