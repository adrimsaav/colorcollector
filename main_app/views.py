from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Color

# Create your views here.
# colors = [
#   {'name': 'Viva Magenta', 'description': 'bright, vivid shade of purplish-red', 'year': 2023},
#   {'name': 'Very Peri', 'description': 'warm periwinkle, a bold lavender', 'year': 2022},
#   {'name': 'Illuminating', 'description': 'bright, cheerful yellow', 'year': 2021},
#   {'name': 'Ultimate Gray', 'description': 'timeless stone gray', 'year': 2021},
#   {'name': 'Classic Blue', 'description': 'a rich, mid-tone blue', 'year': 2020},
#   {'name': 'Living Coral', 'description': 'pinkish red-orange with golden undertone', 'year': 2019},
#   {'name': 'Ultra Violet', 'description': 'enchanting purple with blue undertones', 'year': 2018},
#   {'name': 'Greenery', 'description': 'fresh and zesty yellow-green', 'year': 2017},
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def colors_index(request):
  colors = Color.objects.all()
  return render(request, 'colors/index.html', {
    'colors': colors
  })

def colors_detail(request, color_id):
  color = Color.objects.get(id=color_id)
  return render(request, 'colors/detail.html', {
    "color": color
    })  

class ColorCreate(CreateView):
  model = Color
  fields = '__all__'

class ColorUpdate(UpdateView):
  model = Color
  fields = ['description', 'year']

class ColorDelete(DeleteView):
  model = Color
  success_url = "/colors"