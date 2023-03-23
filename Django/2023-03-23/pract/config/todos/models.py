from django.db import models

# Create your models here.
class Todo(models.Model):
    '''
     
    '''
    task         = models.CharField(max_length=500) # todo 항목
    isCompleted  = models.BooleanField(default=False) # 완료 여부
    created_at   = models.DateTimeField(auto_now_add=True) # 생성 시간
    completed_at = models.DateTimeField(auto_now=True) # 완료시간