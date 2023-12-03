from django.contrib import admin
from .models import Color, Mixing, Vote

# Register your models here.
admin.site.register(Color)
admin.site.register(Mixing)
admin.site.register(Vote)
