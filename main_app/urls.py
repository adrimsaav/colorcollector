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
  path('stars/', views.StarList.as_view(), name='stars_index'),
  path('stars/<int:pk>/', views.StarDetail.as_view(), name='stars_detail'),
  path('colors/<int:color_id>/assoc_star/<int:vote_id>/', views.assoc_star, name='assoc_star'),
  path('colors/<int:color_id>/unassoc_star/<int:vote_id>/', views.unassoc_star, name='unassoc_star'),
  path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
  path('stars/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
  path('stars/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),

]