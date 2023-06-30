from django.db import models

# Create your models here.
class Testcase(models.Model):
    problem_number = models.CharField(max_length=100)
    test_input = models.TextField()
    test_output = models.TextField()

class Usercode(models.Model):
    problem_number = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    user_code = models.TextField()