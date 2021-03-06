import datetime
from django.db import models

# Create your models here.

class BlogPosts(models.Model):
    postId = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    title = models.CharField(max_length=15)
    body = models.TextField()

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    date = models.DateField()
    author = models.CharField(max_length=15)
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=500)
    postId = models.ForeignKey(BlogPosts)

class Gave(models.Model):
    beskrivelse = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True)
    kjopt = models.BooleanField(default=False)

    def __unicode__(self):
     	return self.beskrivelse

    class Meta:
	ordering = ['id']

    class Admin:
    	pass
