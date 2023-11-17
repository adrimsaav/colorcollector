from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('colors/', views.colors_index, name='index'),
  path('colors/<int:color_id>/', views.colors_detail, name='detail'),
  path('colors/create/', views.ColorCreate.as_view(), name='colors_create'),
  path('colors/<int:pk>/update/', views.ColorUpdate.as_view(), name='colors_update'),
  path('colors/<int:pk>/delete/', views.ColorDelete.as_view(), name='colors_delete')
]