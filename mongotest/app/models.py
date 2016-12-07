from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField



class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    tags = ListField()
    comments = ListField(EmbeddedModelField('Comment'))
    
class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    author = EmbeddedModelField('Author')
    text = models.TextField(max_length=200)
    
class Author(models.Model):
    name = models.CharField(max_length=200)