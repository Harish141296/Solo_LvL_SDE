from django.core.management.base import BaseCommand 
from tracker.models import Quest, PenaltyMode
from django.utils import timezone 

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today = timezone.localdate() 
        incomplete = Quest.objects.filter(date=today, is_completed=False)

        if incomplete:
            PenaltyMode.objects.update_or_create(
                date=today,
                defaults={'is_triggered':True, 'triggered_at': timezone.now()}
            )
            self.stdout.write("Penalty mode triggered for today")
        else:
            self.stdout.write("No penalty today - Good Job !")