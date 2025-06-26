from django.shortcuts import render, redirect, get_object_or_404
from .models import Quest, DailyFocusTime
import json 
from django.utils import timezone 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def save_focus_time(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        seconds = data.get('seconds', 0 )
        today = timezone.localdate() # IST 
        obj, _ = DailyFocusTime.objects.get_or_create(date=today)
        obj.seconds_spend = seconds 
        obj.save() 
        return JsonResponse({'status':'success', 'seconds': obj.seconds_spend})
    
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
