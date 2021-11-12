#from django.db import models
#from datetime import date

#class Post(models.Model):
    #titulo = models.CharField(max_length=100)
    #texto = models.TextField()
    #autor= models.CharField(max_length=100)
    #data_publicação = models.DateField(auto_now=True)

#class Blog(models.Model):
    #posts = models.ForeignKey(Post, on_delete=models.CASCADE)    
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title