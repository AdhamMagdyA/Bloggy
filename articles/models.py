from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default= 'default.png', blank=True)
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

    def snippet(self):
        return self.body[:200] + '...'