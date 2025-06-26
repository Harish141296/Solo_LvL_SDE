from django.db import models
from django.utils import timezone 

class DailyFocusTime(models.Model):
    date = models.DateField(default=timezone.now, unique = True) 
    seconds_spend = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.seconds_spend} seconds"
    
class Quest(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    date = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.title} - {'✅' if self.is_completed else '❌'}"