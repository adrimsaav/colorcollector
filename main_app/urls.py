from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('colors/', views.colors_index, name='index'),
  path('colors/<int:color_id>/', views.colors_detail, name='detail'),
  path('colors/create/', views.ColorCreate.as_view(), name='colors_create'),
  path('colors/<int:pk>/update/', views.ColorUpdate.as_view(), name='colors_update'),
  path('colors/<int:pk>/delete/', views.ColorDelete.as_view(), name='colors_delete'),
  path('colors/<int:color_id>/add_mixing_color', views.add_mixing_color, name='add_mixing_color'),
  path('colors/<int:color_id>/assoc_vote/<int:vote_id>/', views.assoc_vote, name='assoc_vote'),
  path('colors/<int:color_id>/unassoc_vote/<int:vote_id>/', views.unassoc_vote, name='unassoc_vote'),
  path('votes/create/', views.VoteCreate.as_view(), name='votes_create'),
  path('votes/<int:pk>/update/', views.VoteUpdate.as_view(), name='votes_update'),
  path('votes/<int:pk>/delete/', views.VoteDelete.as_view(), name='votes_delete'),

]