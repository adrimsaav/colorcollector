from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Color, Vote
from .forms import MixingForm

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
  id_list = color.votes.all().values_list('id')
  votes_color_doesnt_have = Vote.objects.exclude(id__in=id_list)
  mixing_form = MixingForm()
  return render(request, 'colors/detail.html', {
    'color': color, 'mixing_form': mixing_form
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


def assoc_vote(request, color_id, vote_id):
  Color.objects.get(id=color_id).votes.add(vote_id)
  return redirect('detail', color_id=color_id)

def unassoc_vote(request, color_id, vote_id):
  Color.objects.get(id=color_id).votes.remove(vote_id)
  return redirect('detail', color_id=color_id)

def add_mixing_color(request, color_id):
  form = MixingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_mixing_color = form.save(commit=False)
    new_mixing.color_id = color_id
    new_mixing_color.save()
  return redirect('detail', color_id=color_id)


class VoteCreate(CreateView):
  model = Vote
  fields = '__all__'

class VoteUpdate(UpdateView):
  model = Vote
  fields = ['name', 'votes']

class VoteDelete(DeleteView):
  model = Vote
  success_url = '/votes'

