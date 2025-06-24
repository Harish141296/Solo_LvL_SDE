from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('complete/<int:quest_id>/', views.complete_quest, name='complete_quest'),
]
