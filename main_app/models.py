from django.db import models
from django.urls import reverse

MIXING_COLORS = (
  ('R', 'Red'),
  ('B', 'Blue'),
  ('Y', 'Yellow'),
)

# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length=3)
    votes = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('votes_detail', kwargs={'pk': self.id})

class Color(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    votes = models.ManyToManyField(Vote)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'color_id': self.id})


class Mixing(models.Model):
    date = models.DateField('mixing date')
    mix = models.CharField(
        max_length=1,
            choices = MIXING_COLORS,
            default = MIXING_COLORS[0][0])

    # color_id FK
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_mix_display()} on {self.date}"

    class Meta:
        ordering = ['-date']