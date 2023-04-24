from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} : {self.title}'


class Review(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} Review - {self.music.title}'