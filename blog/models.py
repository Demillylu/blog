from django.db import models
from datetime import date

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor= models.CharField(max_length=100)
    data_publicação = models.DateField(auto_now=True)

class Blog(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)      

