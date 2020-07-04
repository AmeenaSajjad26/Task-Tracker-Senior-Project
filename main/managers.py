from django.db import models
from django.conf import settings

class PostQuerySet(models.QuerySet):
    def get_users_activity(self,username):
        return self.filter(activityuser__username=username)
        

class activitymanager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using =self._db)
    def get_users_activity(self, username):
        return self.get_queryset().get_users_activity(username)
    def check_activity_time(self,weekday,currenttime,username):
        return self.filter(starttime__lte=currenttime ,endtime__gte=currenttime,repeat__contains=weekday,activityuser__username=username)
        