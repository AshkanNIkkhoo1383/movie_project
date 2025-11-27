import django
from django.db import models
from django.db.models.fields import TextField 
import uuid 


class Filmcritic(models.Model): 
    pass 
class Director(models.Model):
    pass
class Actor(models.Model): 
    pass 
class PhotosofTheActors(models.Model): 
    pass 
class Movie(models.Model): 
    Movie_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Title = models.CharField(max_length=200) 
    Description = models.TextField(blank=True) 
    Poster = models.BinaryField(blank=True,null=True) 
    Trailer = models.BinaryField(blank=True,null=True)  
class MusicAlbum(models.Model):
    pass 
class ImageGallery(models.Model):
    pass
class Comment(models.Model): 
    pass 