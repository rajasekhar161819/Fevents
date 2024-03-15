from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.TextField()
    event_image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    is_liked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name