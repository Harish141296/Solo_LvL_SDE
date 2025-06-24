from django.shortcuts import render
from .models import Quest 
from django.utils import timezone 

def home(request):
    today = timezone.now().date()
    quests = Quest.objects.filter(date=today)
    return render(request, 'tracker/home.html', {'quests': quests})
