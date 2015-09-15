from django.db import models


 
# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('Date Published')
    def __str__(self):
        return self.text