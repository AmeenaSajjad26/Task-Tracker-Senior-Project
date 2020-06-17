from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    taskname= models.CharField(max_length=100)
    tasktype= models.CharField(max_length=100)
    duedate= models.DateField()
    estimatetime= models.PositiveIntegerField()
    taskuser =models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.taskname

    def get_absolute_url(self):
        return reverse('task-detail',kwargs={'pk':self.pk})

class Activity(models.Model):
    MY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    activityname= models.CharField(max_length=100)
    starttime= models.TimeField()
    endtime= models.TimeField()
    repeat = models.CharField(max_length=100, choices=MY_CHOICES)
    activityuser =models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.activityname

    def get_absolute_url(self):
        return reverse('activity-detail',kwargs={'pk':self.pk})