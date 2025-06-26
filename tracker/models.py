from django.db import models
from django.utils import timezone 

class DailyFocusTime(models.Model):
    date = models.DateField(default=timezone.now, unique = True) 
    seconds_spend = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.seconds_spend} seconds"
    
class PenaltyMode(models.Model):
    date = models.DateField(default=timezone.now, unique = True)
    is_triggered = models.BooleanField(default=False)
    triggered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.date}-{'Active' if self.is_triggered else 'Clear'}"
class Quest(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    date = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.title} - {'✅' if self.is_completed else '❌'}"