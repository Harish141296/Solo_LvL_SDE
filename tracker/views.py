from django.shortcuts import render, redirect, get_object_or_404
from .models import Quest, DailyFocusTime
import json 
import random 
from datetime import datetime, timedelta 
from django.utils import timezone 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt

TOP_SDE_REWARDS = [
    "Master Python's `functools.lru_cache` for blazing-fast memoization",
    "Use `git bisect` to find bugs quickly between commits",
    "AI Pro Tip: Learn vector databases like FAISS or Weaviate",
    "Use `__slots__` in Python classes to save memory",
    "Dockerize your apps with multi-stage builds for smaller image size"
]
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
    # Last 7 days focus time 
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    focus_data = [] 
    for d in last_7_days:
        obj = DailyFocusTime.objects.filter(date=d).first()
        seconds = obj.seconds_spend if obj else 0 
        focus_data.append({'date': d.strftime("%a"), 'minutes': round(seconds/60)})
    #reward 
    reward_tip = None 
    focus_today = DailyFocusTime.objects.filter(date=today).first()
    if focus_today and focus_today.seconds_spend >= 3600:
        reward_tip = random.choice(TOP_SDE_REWARDS)

    return render(request, 'tracker/home.html', {
        'quests': quests,
        'completed_count': completed_count,
        'total_count': total_count,
        'focus_time_data': focus_data,
        'reward_tip': reward_tip,
        })

def complete_quest(request, quest_id):
    quest = get_object_or_404(Quest, id=quest_id)
    quest.is_completed = True 
    quest.save() 
    return redirect('home') 
