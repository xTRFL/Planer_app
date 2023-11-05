from django.shortcuts import render
from django.http import Http404, HttpResponse
import requests
from django.db.models import Max

from .models import *

def index(request):
    return render(request, 'home.html')

def detail(request, quest_id):
    quest_id2 = quest_id
    while True:
        try:
            quest = PlanerQuest.objects.get(user_id = request.user.id, quest_id = quest_id)
            break
        except PlanerQuest.DoesNotExist:
            quest_id = PlanerQuest.objects.filter(user_id = request.user.id).aggregate(max_value = Max('quest_id'))['max_value']
    return render(request, 'detail.html', {'quest': quest, 'id': quest_id2})

def planer(request):
    user_plans = PlanerQuest.objects.get(pk = request.user.id)
    return render(request, 'home.html')


def add_quest(request):
    quest = PlanerQuest()
    return render(request, 'home.html', {'quest': quest})

def show_user_quests(request):
    quests = PlanerQuest.objects.filter(user_id = request.user.id)
    return render(request, 'quest.html', {'quests': quests})

# def show_user_quest(request, quest_id):
#     response = PlanerQuest.objects.get(quest_id = quest_id)
#     text = f"""
#             <h1>{response.title}</h1>
#             <p>{response.description}</p>
#             """
#     return HttpResponse(text, content_type='text/plain')

# def render_quest(request, quest_id):
#     response = PlanerQuest.objects.get(quest_id = quest_id)
#     return render(request, 'quest.html', {'quest': response})


