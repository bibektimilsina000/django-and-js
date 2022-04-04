from optparse import TitledHelpFormatter
from django.db import models
from django.forms import Textarea


class Post(models.Model):

    title = models.CharField( max_length=50)
    content = models.TextField()
    author = models.ForeignKey( on_delete=models.CASCADE)
    
    
    

    def __str__(self):
        return self.title




# Create your models here.
