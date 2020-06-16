from django.db import models

# Create your models here.
class User(models.Model):
    EventID = models.AutoField(primary_key=True),
    username = models.CharField(max_length=50, name='event_name')
    password = models.CharField(max_length=50, name='event_name')
    email = models.CharField(max_length=50, name='event_name')
    last_login_time = models.TimeField()


    def __str__(self):
        return self.event_name

class Suggestion(models.Model):
    suggestionID = models.AutoField(primary_key=True),
    breakfast_time = models.TimeField()
    lunch_time = models.TimeField()
    dinner_time = models.TimeField()
    sleep_time = models.TimeField()
    relax_time = models.TimeField()
    work_time = models.TimeField()
    exercise_time = models.TimeField()

    def __str__(self):
        return self.event_name

class Task(models.Model):
    taskID = models.AutoField(primary_key=True),
    task_name = models.CharField(max_length=50, name='event_name')
    due_date = models.DateField()
    task_type = models.CharField(max_length=50, name='event_name')
    estimated_time = models.TimeField()


    def __str__(self):
        return self.event_name

class LongTermSchedule(models.Model):
    EventID = models.AutoField(primary_key=True),
    event_name = models.CharField(max_length=50, name='event_name')
    start_time = models.TimeField()
    end_time = models.TimeField()
    taskID = models.AutoField(primary_key=True)
    EventID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.event_name