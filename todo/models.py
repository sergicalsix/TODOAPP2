from django.db import models
from django.urls import reverse

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField() #CharFieldより長い
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
