from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.
class Task(models.Model):
    MY_CHOICES = (
        ('Small', 'Small'),
        ('Middle', 'Middle'),
        ('Large', 'Large'),
    )
    STATUS_CHOICES = (
    ('OnProgress', 'OnProgress'),
    ('Done', 'Done'),
)
    taskname= models.CharField(max_length=100)
    tasktype= models.CharField(max_length=10,choices=MY_CHOICES)
    duedate= models.DateField(default=timezone.now)
    spenttime= models.PositiveIntegerField(default=1)
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default="OnProgress")
    taskuser =models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.taskname

    def get_absolute_url(self):
        return reverse('task-detail',kwargs={'pk':self.pk})
    
    def get_status(self): 
        return self.status

class Activity(models.Model):
    MY_CHOICES = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    activityname= models.CharField(max_length=100)
    starttime= models.PositiveIntegerField()
    endtime= models.PositiveIntegerField()
    repeat = MultiSelectField(choices=MY_CHOICES)
    activityuser =models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.activityname

    def get_absolute_url(self):
        return reverse('activity-detail',kwargs={'pk':self.pk})

class Schedule(models.Model):
    date = models.DateField()
    timeslot = models.CharField(max_length=100)
    eventname =models.CharField(max_length=100)
    objects = models.Manager()

