from django.db import models
from django.contrib.auth.models import User

class schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username) + ' -- ' + str(self.topic)