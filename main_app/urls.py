from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('colors/', views.colors_index, name='index'),
  path('colors/<int:color_id>/', views.colors_detail, name='detail')
]