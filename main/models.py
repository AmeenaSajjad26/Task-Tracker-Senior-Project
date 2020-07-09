from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .managers import activitymanager
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator

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
    spenthour= models.PositiveIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    spentmin= models.PositiveIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(60)])
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default="OnProgress")
    taskuser =models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.taskname

    def get_absolute_url(self):
        return reverse('task-detail',kwargs={'pk':self.pk})

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
    starttime= models.PositiveIntegerField(default=7,validators=[MinValueValidator(7), MaxValueValidator(18)])
    endtime= models.PositiveIntegerField(default=8,validators=[MinValueValidator(8), MaxValueValidator(19)])
    repeat = MultiSelectField(choices=MY_CHOICES)
    activityuser =models.ForeignKey(User, on_delete=models.CASCADE)
    objects = activitymanager()

    def __str__(self):
        return self.activityname

    def get_absolute_url(self):
        return reverse('activity-detail',kwargs={'pk':self.pk})
