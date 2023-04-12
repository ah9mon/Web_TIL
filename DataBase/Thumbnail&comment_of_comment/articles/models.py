from django.db import models
from imagekit.processors import Thumbnail, ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField


# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=30,unique=True) 

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    thumbnail_img = ImageSpecField(
        source = 'image', 
        processors = [Thumbnail(200,300)], # 200X300 으로 줄이자 
        format = 'JPEG',
        options = {'quality':80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, 
        null = True,
        related_name='replies',
        ) # 답글 구현할 때 parent라는 field로 많이 함 


