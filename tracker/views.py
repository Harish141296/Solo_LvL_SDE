from django.shortcuts import render, redirect, get_object_or_404
from .models import Quest 
from django.utils import timezone 

def home(request):
    today = timezone.now().date()
    quests = Quest.objects.filter(date=today).order_by('id')
    completed_count = quests.filter(is_completed=True).count()
    total_count = quests.count()
    return render(request, 'tracker/home.html', {
        'quests': quests,
        'completed_count': completed_count,
        'total_count': total_count
        })

def complete_quest(request, quest_id):
    quest = get_object_or_404(Quest, id=quest_id)
    quest.is_completed = True 
    quest.save() 
    return redirect('home') 
