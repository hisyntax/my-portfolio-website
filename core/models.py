from tinymce import  HTMLField
from django.db import models
from django.urls import reverse




class Picture(models.Model):
    title = models.CharField(max_length=100, default="cv")
    picture = models.FileField(upload_to='profile', default="Profile_pics")

    def __str__(self):
        return self.title

class Cv(models.Model):
    title = models.CharField(max_length=100, default="cv")
    cv = models.FileField(upload_to='cv')

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    overview = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.FileField(upload_to='images')
    django = models.BooleanField(default=False, blank=True)
    sqlite = models.BooleanField(default=False, blank=True)
    golang = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={
            'id': self.id
        })

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Project(models.Model):
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.FileField(upload_to='images')
    django = models.BooleanField(default=False, blank=True)
    sqlite = models.BooleanField(default=False, blank=True)
    golang = models.BooleanField(default=False, blank=True)
    featured = models.BooleanField(default=False, blank=True)
    url = models.CharField(max_length=500)
    template = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.overview

class About(models.Model):
    title = models.CharField(max_length=200, default="About me")
    overview = models.TextField()

    def __str__(self):
        return self.title
