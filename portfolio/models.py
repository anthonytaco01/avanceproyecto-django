from django.db import models
from django.db.models.fields import CharField,URLField
from django.db.models.fields import Imagefield

class Projects(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=100)
    image = Imagefield(upload_to='portafolio/images/')
    url = URLField(blank=True)
