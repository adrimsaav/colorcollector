from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Color, Star
from .forms import MixingForm

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
  stars = Star.objects.all()
  id_list = color.stars.all().values_list('id')
  stars_color_doesnt_have = Star.objects.exclude(id__in=id_list)
  mixing_form = MixingForm()
  return render(request, 'colors/detail.html', {
    'color': color, 'mixing_form': mixing_form,
    'stars': stars_color_doesnt_have

  })

class ColorCreate(CreateView):
  model = Color
  fields = ['name', 'description', 'year']

class ColorUpdate(UpdateView):
  model = Color
  fields = ['description', 'year']

class ColorDelete(DeleteView):
  model = Color
  success_url = "/colors"

def add_mixing_color(request, color_id):
  form = MixingForm(request.POST)
  if form.is_valid():
    new_mixing = form.save(commit=False)
    new_mixing.color_id = color_id
    new_mixing.save()
    
  return redirect('detail', color_id=color_id)

class StarList(ListView):
  model = Star

class StarDetail(DetailView):
  model = Star

class StarCreate(CreateView):
  model = Star
  fields = '__all__'

class StarUpdate(UpdateView):
  model = Star
  fields = ['review', 'stars']

class StarDelete(DeleteView):
  model = Star
  success_url = '/stars'

def assoc_star(request, color_id, star_id):
  Color.objects.get(id=color_id).stars.add(star_id)
  return redirect('detail', color_id=color_id)

def unassoc_star(request, color_id, star_id):
  Color.objects.get(id=cat_id).stars.remove(star_id)
  return redirect('detail', color_id=color_id)


